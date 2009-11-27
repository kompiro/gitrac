#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Hiroki Kondo (aka.kompiro)
# All rights reserved.

from setuptools import setup

setup(
    name = 'gitrac',
    version = '0.0.2',
    description = 'distributed Trac Ticket repository like git',
    author = 'Hiroki Kondo',
    author_email = 'kompiro@gmail.com',
    license = 'EPL',
    url = 'http://github.com/kompiro/gitrac',
    download_url = 'http://github.com/kompiro/gitrac/downloads',
    packages = ['gitrac'],
    entry_points = """
        [console_scripts]
        gitrac = gitrac.main:main
    """,
)
