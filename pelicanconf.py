#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'eijit'
SITENAME = 'eijit\'s blog'
SITEURL = 'https://eijit.github.io'
# SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Twitter',   'https://twitter.com/eijit'),
    ('GitHub',    'https://github.com/eijit'),
    ('Bookmeter', 'https://bookmeter.com/users/13752'),
)

# DEFAULT_PAGINATION = 10
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    'pelican-toc',
    'render_math',
    'series'
]

THEME = './themes/elegant'

STATIC_PATHS = ['images']
