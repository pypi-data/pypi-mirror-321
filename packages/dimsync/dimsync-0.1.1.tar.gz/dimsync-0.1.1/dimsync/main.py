import json
import logging
import os.path
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
    _p.add_argument('--version', action='version', version='dockerman 0.1.0')
    _p.add_argument(
        'command',
        choices=[
            'config',
            'fetch',
            'sync',
            'start',
            'stop',
            'restart',
            'logs',
            'status',
            'build',
            'run',
            'rm',
            'pull',
            'push',
            'images',
            'ps',
            'inspect',
            'volumes',
            'compose',
        ],
    )
    _p.add_argument('-d', '--detached', action='store_true', help='Run container in detached mode')
    _p.add_argument('-t', '--tag', help='Specify a tag for the image')
    _p.add_argument('-i', '--interactive', action='store_true', help='Keep STDIN open even if not attached')
    _p.add_argument('-p', '--publish', help='Publish a container\'s port(s) to the host')
    _p.add_argument('-v', '--volume', help='Bind mount a volume from the host to a container')
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

    def rmi(self, **kwargs):
        repo = kwargs.get('repo')
        tag = kwargs.get('tag')
        plat = '{}/{}'.format(kwargs.get('os'), kwargs.get('arch'))
        print(f'Removing {repo}:{tag}, platform={plat}')
        self.client.images.remove(f'{repo}:{tag}')


def _config(args):
    print(args)


def _fetch(args):
    config = Config()
    try:
        docker = Docker()
        cache = Cache()
        images = cache.sort(docker.images())
        for image in images:
            if isinstance(config.registry, str) and image.get('repo').startswith(config.registry + '/'):
                docker.rmi(**image)
                continue
            if not image.get('exist'):
                config.debug() and print('Skipped: image {}:{} not exist'.format(image.get('repo'), image.get('tag')))
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


def main():
    args = _parser().parse_args()
    if args.command == 'config':
        _config(args)
    elif args.command == 'fetch':
        _fetch(args)


if __name__ == '__main__':
    main()
