#!/usr/bin/python3
# -*- mode: python; coding: utf-8 -*-

from distutils.core import setup


def get_version():
    with open('debian/changelog', errors="ignore") as chlog:
        return chlog.readline().split()[1][1:-1]

setup(
    name          = 'elasticsearch2',
    version       =  get_version(),
    description   = "Official low-level client for Elasticsearch",
    author        = "Honza Král",
    url           = "https://github.com/elastic/elasticsearch-py",
    packages      = [
        'elasticsearch',
        'elasticsearch.client',
        'elasticsearch.connection',
        'elasticsearch.helpers',
        'elasticsearch2',
        'elasticsearch2.client',
        'elasticsearch2.connection',
        'elasticsearch2.helpers',
    ],
)
