# -*- encoding: utf-8 -*-
from setuptools import setup

setup(
    name="threebot-crypto",
    packages=['threebot_crypto'],
    version="1.1.0",
    author_email="wagner@arteria.ch",
    maintainer_email="admin@arteria.ch",
    install_requires=open('requirements.txt').read().split('\n'),
)
