# -*- coding: utf-8 -*-
#14-6-11
# create by: snower

from setuptools import setup

setup(
    name='torthrift',
    version='0.1.4',
    packages=['torthrift','torthrift.server','torthrift.transport'],
    package_data={
        '': ['README.rst'],
    },
    install_requires=['thrift>=0.9.1','tornado>=3.2.1', 'greenlet>=0.4.2',],
    author='snower',
    author_email='sujian199@gmail.com',
    url='http://github.com/snower/TorThrift',
    license='MIT',
    description='Tornado asynchronous thrift server and client',
    long_description='torthrift - presents a Tornado Future-based API and greenlet for non-blocking thrift server and client.'
)
