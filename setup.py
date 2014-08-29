# -*- encoding: utf-8 -*-

from setuptools import setup
import threebot_crypto as app

setup(
    name = "threebot-crypto",
    version = app.__version__,
    install_requires=[
        "pycrypto>=2.6.1",
    ],
)