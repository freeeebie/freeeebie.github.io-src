#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "pelican-themes/pelican-bootstrap3"
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites', 'render_math', 'ipynb.markup']
IPYNB_USE_META_SUMMARY = True

PLUGINS += ['summary']
SUMMARY_BEGIN_MARKER = '<!-- PELICAN_BEGIN_SUMMARY -->'
SUMMARY_END_MARKER = '<!-- PELICAN_END_SUMMARY -->'

IGNORE_FILES = ['.ipynb_checkpoints']
CACHE_CONTENT = True

LOAD_CONTENT_CACHE = False
MATH_JAX = {'align': 'left',
            'indent': '2em',
            'responsive': True,
            'autoNumber': 'AMS'}

AUTHOR = 'freeeebie'
SITENAME = 'Log'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
#('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/freeeebie'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
