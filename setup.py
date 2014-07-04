# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst') as f:
    description = f.read()


setup(
    name='lymph',
    url='http://github.com/deliveryhero/lymph/',
    version='0.1.0',
    namespace_packages=['lymph'],
    packages=find_packages(),
    license=u'Apache License (2.0)',
    author=u'Delivery Hero Holding GmbH',
    maintainer=u'Johannes Dollinger',
    maintainer_email=u'johannes.dollinger@deliveryhero.com',
    long_description=description,
    include_package_data=True,
    setup_requires=[
#        'Cython>=0.20.1',
    ],
    install_requires=[
        'docopt>=0.6.1',
        'gevent>=1.1-dev',
        'kazoo>=1.3.1',
        'kombu>=3.0.16',
        'monotime>=1.0', # FIXME: only for Python 2
        'msgpack-python>=0.4.0',
        'psutil>=2.1.1',
        'PyYAML>=3.11',
        'pyzmq>=14.3.0',
        'redis>=2.9.1',
        'setproctitle>=1.1.8',
        'six>=1.6',
        'Werkzeug>=0.9.4',
        'blessings>=1.5.1',
    ],
    entry_points={
        'console_scripts': ['lymph = lymph.cli.main:main'],
        'lymph.cli': [
            'help = lymph.cli.help:HelpCommand',
            'list = lymph.cli.base:ListCommand',
            'tail = lymph.cli.tail:TailCommand',
            'instance = lymph.cli.service:InstanceCommand',
            'node = lymph.cli.service:NodeCommand',
            'request = lymph.cli.request:RequestCommand',
            'discover = lymph.cli.request:DiscoverCommand',
            'inspect = lymph.cli.request:InspectCommand',
            'subscribe = lymph.cli.request:SubscribeCommand',
            'emit = lymph.cli.request:EmitCommand',
        ],
        'nose.plugins.0.10': ['lymph = lymph.testing.nose:LymphPlugin'],
        'pytest11': ['lymph = lymph.testing.pytest'],
        'kombu.serializers': [
            'lymph-json = lymph.serializers.kombu:json_serializer_args',
            'lymph-msgpack = lymph.serializers.kombu:msgpack_serializer_args',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ]
)
