from setuptools import setup, find_packages
import pathlib

setup(
    name='dimsync',
    version='0.1.1',
    author='HSIAOLIN',
    author_email='sjzshmh@gmail.com',
    description='An easy-to-use docker image management tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eptr/dockerman',
    packages=find_packages(pathlib.Path(__file__).parent.resolve()),
    install_requires=[
        'docker',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8, <4',
    entry_points={
        'console_scripts': [
            'dimsync=dimsync.main:main',
        ],
    },
)
