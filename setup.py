# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '1.1.0'

setup(
    name='pickit',
    version=version,
    packages=find_packages(),
    entry_points={
        "console_scripts": {
            "pcat=pickit._pcat:main",
        }
    },
    url="https://github.com/akahana-1/pickit",
    author="akahana-1",
    author_email="aakahana@gmail.com",
    description="Simple pickle iteration tool.",
)
