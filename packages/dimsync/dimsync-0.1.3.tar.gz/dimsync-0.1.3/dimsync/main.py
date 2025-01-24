import json
import logging
import os.path
import re
import time
import traceback
from argparse import ArgumentParser
from datetime import datetime
from functools import reduce

from docker.errors import DockerException, ImageNotFound, APIError
from requests.exceptions import HTTPError

logger = logging.getLogger('dockerman')


def _parser():
    _p = ArgumentParser()
    _p.add_argument('--version', action='version', version='dimsync 0.1.0')
    _subs = _p.add_subparsers(dest='command', help='commands')
    # config
    _p_config = _subs.add_parser('config', help='get or set config')
    _subs_config = _p_config.add_subparsers(dest='subcommand', help='subcommand')
    _subs_config.add_parser('ls')
    _p_config_get = _subs_config.add_parser('get')
    _p_config_get.add_argument('key')
    _p_config_set = _subs_config.add_parser('set')
    _p_config_set.add_argument('key')
    _p_config_set.add_argument('value')
    _p_config_unset = _subs_config.add_parser('unset')
    _p_config_unset.add_argument('key')
    _p_config_add = _subs_config.add_parser('add')
    _p_config_add.add_argument('key')
    _p_config_add.add_argument('value')
    _p_config_del = _subs_config.add_parser('del')
    _p_config_del.add_argument('key')
    _p_config_del.add_argument('value')
    # fetch
    _p_fetch = _subs.add_parser('fetch', help='fetch updates')
    _p_fetch.add_argument('pattern', nargs='?', help='name or pattern')
    # sync
    _p_sync = _subs.add_parser('sync', help='push updates to registry')
    _p_sync.add_argument('pattern', nargs='?', help='name or pattern')
    _p_sync.add_argument('registry', nargs='?', help='registry')
    return _p


def _help():
    _parser().print_help()


def _data_dir():
    return os.path.expanduser('~/.docker')


class Config(object):
    def __init__(self):
        self.data = {}
        file = os.path.join(_data_dir(), 'dm_config')
        if not os.path.isfile(file):
            return
        with open(file, 'r') as f:
            data = json.load(f)
        if isinstance(data, dict):
            self.data = data

    @property
    def retry(self):
        return self.get('retry', 3)

    @property
    def registry(self):
        return self.get('registry', None)

    def debug(self):
        return self.get('debug', False)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value

    def save(self):
        os.makedirs(_data_dir(), exist_ok=True)
        file = os.path.join(_data_dir(), 'dm_config')
        with open(file, 'w') as f:
            json.dump(self.data, f, indent=4)


class Cache(object):
    def __init__(self):
        self.data = {}
        file = os.path.join(_data_dir(), 'dm_cache')
        if not os.path.isfile(file):
            return
        with open(file, 'r') as f:
            data = json.load(f)
        if isinstance(data, dict):
            self.data = data

    def get(self, **kwargs):
        repo = kwargs.get('repo')
        tag = kwargs.get('tag')
        plat = '{}/{}'.format(kwargs.get('os'), kwargs.get('arch'))
        if repo in self.data and tag in (r := self.data.get(repo)) and plat in (r := r.get(tag)):
            return r.get(plat)
        return None

    def set(self, **kwargs):
        keys = [kwargs.get('repo'), kwargs.get('tag'), '{}/{}'.format(kwargs.get('os'), kwargs.get('arch'))]
        value = {k: v for k, v in kwargs.items() if k not in ['repo', 'tag', 'os', 'arch']}
        value.update({'atime': datetime.now().isoformat()})
        reduce(lambda d, k: d.setdefault(k, {}), keys, self.data).update(value)
        self.save()

    def sort(self, images):
        for image in images:
            hist = self.get(**image)
            if hist:
                image['atime'] = hist.get('atime')
                image['exist'] = hist.get('exist', True)
            else:
                image['atime'] = datetime.fromtimestamp(0).isoformat()
        return sorted(images, key=lambda x: datetime.fromisoformat(x['atime']))

    def save(self):
        os.makedirs(_data_dir(), exist_ok=True)
        file = os.path.join(_data_dir(), 'dm_cache')
        with open(file, 'w') as f:
            json.dump(self.data, f, indent=4)


class Docker(object):
    def __init__(self):
        import docker

        self.client = docker.from_env()

    def _image_info(self, image):
        return [
            {
                'repo': x.split(':')[0],
                'tag': x.split(':')[1],
                'os': image.attrs.get('Os'),
                'arch': image.attrs.get('Architecture'),
                'id': image.id.removeprefix('sha256:'),
                'ctime': image.attrs.get('Created'),
                'size': image.attrs.get('Size'),
            }
            for x in image.tags
        ]

    def images(self):
        return [y for x in self.client.images.list() for y in self._image_info(x)]

    def tag(self, src, **kwargs):
        image = self.client.images.get(src)
        if image is None:
            return
        image.tag(kwargs.get('repo'), tag=kwargs.get('repo'))

    def pull(self, **kwargs):
        repo = kwargs.get('repo')
        tag = kwargs.get('tag')
        plat = '{}/{}'.format(kwargs.get('os'), kwargs.get('arch'))
        print(f'Pulling {repo}:{tag}, platform={plat}')
        image = self.client.images.pull(repo, tag=tag, platform=plat)
        data = self._image_info(image)
        if len(data) == 0:
            raise ValueError('Pull return empty image')
        elif len(data) > 1:
            raise ValueError(f'Pull return multiple images: {data}')
        data = data[0]
        if kwargs.get('id') != data.get('id'):
            print(f'  Downloaded newer image for {repo}:{tag}')
        else:
            print(f'  Image is up to date for {repo}:{tag}')
        print(f'  Digest: {image.id}')
        return data

    def push(self, **kwargs):
        repo = kwargs.get('repo')
        tag = kwargs.get('tag')
        image = self.client.images.get(f'{repo}:{tag}')
        if image is None:
            print(f'Error: Image {repo}:{tag} not found')
            return
        print(f'Pushing {repo}:{tag}')
        self.client.images.push(repo, tag)
        print(f'  Digest: {image.id}')

    def rmi(self, **kwargs):
        repo = kwargs.get('repo')
        tag = kwargs.get('tag')
        plat = '{}/{}'.format(kwargs.get('os'), kwargs.get('arch'))
        print(f'Removing {repo}:{tag}, platform={plat}')
        self.client.images.remove(f'{repo}:{tag}')


def _config(args):
    config = Config()
    config.debug() and print(args)
    if args.subcommand == 'ls':
        for key, value in config.data.items():
            print(f'{key}: {value}')
    elif args.subcommand == 'get':
        print(f'{args.key}:', config.get(args.key))
    elif args.subcommand == 'set':
        config.set(args.key, args.value)
        config.save()
    elif args.subcommand == 'unset':
        config.data.pop(args.key, None)
        config.save()
    elif args.subcommand == 'add':
        if isinstance(config.data[args.key], list):
            config.data[args.key].append(args.value)
        else:
            config.data[args.key] = [args.value]
        config.save()
    elif args.subcommand == 'del':
        if isinstance(config.data[args.key], list):
            config.data[args.key].remove(args.value)
        else:
            config.data.pop(args.key, None)
        config.save()
    else:
        print(f'Invalid subcommand: {args.subcommand}')


def _fetch(args):
    config = Config()
    config.debug() and print(args)
    pattern = args.pattern
    try:
        docker = Docker()
        cache = Cache()
        images = cache.sort(docker.images())
        for image in images:
            name = '{}:{}'.format(image.get('repo'), image.get('tag'))
            if isinstance(config.registry, str) and name.startswith(config.registry + '/'):
                docker.rmi(**image)
                continue
            if isinstance(pattern, str) and re.search(pattern, name) is None:
                continue
            if not image.get('exist'):
                config.debug() and print(f'Skipped: Image {name} not exist')
                continue
            for i in range(1, config.retry + 1):
                try:
                    info = docker.pull(**image)
                    cache.set(**{**info, 'exist': True})
                    continue
                except ImageNotFound:
                    cache.set(**{**image, 'exist': False})
                    print(f'  Failed: Image not found: {image}')
                    continue
                except (APIError, HTTPError):
                    config.debug() and traceback.print_exc()
                    print('  Error: Failed to connect to Docker API' + (', retrying' if i < config.retry else ''))
                    time.sleep(1.5)
    except DockerException:
        config.debug() and traceback.print_exc()
        print('Error: Docker is not installed or not running')
    except Exception:
        config.debug() and traceback.print_exc()


def _sync(args):
    config = Config()
    config.debug() and print(args)
    pattern = args.pattern
    registry = args.registry or config.registry
    if isinstance(registry, str):
        print('Error: Registry not specified')
        return
    try:
        docker = Docker()
        cache = Cache()
        for image in docker.images():
            name = '{}:{}'.format(image.get('repo'), image.get('tag'))
            if isinstance(registry, str) and name.startswith(registry + '/'):
                docker.rmi(**image)
                continue
            if isinstance(pattern, str) and re.search(pattern, name) is None:
                continue
            hist = cache.get(**image)
            if hist and isinstance(r := hist.get('registry'), dict) and r.get(registry) == image.get('id'):
                config.debug() and print(f'Skipped: Image {name} already synced')
                continue
            secs = [x for x in image.get('repo').split('/') if len(x)]
            if len(secs) == 0:
                print(f'Error: Invalid repository name: {name}')
                continue
            if len(secs) > 2:
                secs = secs[-2:]
            elif len(secs) == 1:
                secs.insert(0, 'library')
            if len(secs) != 2:
                print(f'Error: Invalid repository name processing: {secs}')
                continue
            secs.insert(0, registry)
            mirror = {
                'repo': '/'.join(secs),
                'tag': image.get('tag'),
                'os': image.get('os'),
                'arch': image.get('arch'),
            }
            docker.tag(name, **mirror)
            docker.push(**mirror)
            docker.rmi(**mirror)
            hist = hist or {}
            hist.setdefault('registry', {}).update({registry: image.get('id')})
            cache.set(**hist)
    except DockerException:
        config.debug() and traceback.print_exc()
        print('Error: Docker is not installed or not running')
    except Exception:
        config.debug() and traceback.print_exc()


def main():
    args = _parser().parse_args()
    if args.command == 'config':
        _config(args)
    elif args.command == 'fetch':
        _fetch(args)
    elif args.command == 'sync':
        _sync(args)


if __name__ == '__main__':
    main()
