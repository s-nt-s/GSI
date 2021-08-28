#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
from glob import glob
from pathlib import Path
import re

sys.path.append('.')

from myplugins import reader, replacements, mod_html, set_count, mod_content, category_meta
from myplugins.jinja_filters import JINJA_FILTERS

sys.path.append('.')

abspath = os.path.abspath(__file__)
cur_dir = os.path.dirname(abspath)
re_slnu = re.compile(r"/([0-9]+|[A-Z]+)-")

class DynamicSetting(object):
    def __init__(self, f):
        self.f = f

    def format(self, **metadata):
        return self.f(metadata).format(**metadata)


def myglob(root, *args):
    r = []
    for a in args:
        r.extend(glob(root+a))
    return sorted(r)


def rcglob(root, *args):
    ok = []
    ko = []
    root = Path(root)
    for a in args:
        if a.startswith("!"):
            ko.extend(root.rglob("*."+a[1:]))
        else:
            for i in root.rglob("*."+a):
                if i not in ko:
                    ok.append(i)
    return sorted(ok)


AUTHOR = 's-nt-s'
SITENAME = 'Apuntes GSI'
SITEURL = 'https://s-nt-s.github.io/GSI'
GITHUB_URL = 'https://github.com/s-nt-s/GSI'
SOURCE_URL = GITHUB_URL+'/tree/master'
MAPA_URL = 'mapa'

SITEURL = os.environ.get('URL', SITEURL)

# LEN_CUR_DIR se usa para hacer relativas rutas como source_path
LEN_CUR_DIR = len(cur_dir)+1

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('About', 'about'),
    ('Mapa', MAPA_URL),
    ('Ver Github', SOURCE_URL),)

# Social widget
SOCIAL = (
    ('@s-nt-s', 'https://github.com/s-nt-s/'),
)

#DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 0
FEED_ALL_ATOM = 'feeds/all.atom.xml'
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# 'index',
DIRECT_TEMPLATES = ['sitemap', 'map']
AUTHOR_SAVE_AS = False
SITEMAP_SAVE_AS = 'sitemap.xml'
MAP_SAVE_AS = MAPA_URL + '/index.html'

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']


def get_url(metadata):
    path = metadata['path']
    path = path.split(os.path.sep)
    path = path[1:-1]
    arr = []
    if len(path) > 0:
        path = os.path.join(*path)
        arr.append(path)

    isIndex = metadata['slug'] == 'index' or metadata.get('index') == True
    if not isIndex:
        arr.append("{slug}")

    if not arr:
        return "/"

    url = "/".join(arr)
    if isIndex:
        return url + "/"

    url = re_slnu.sub("/", url)
    return url+".html"


def url_to_file(url):
    url = url.rstrip("/")
    if url:
        if url.endswith(".html"):
            return url
        return url + "/index.html"
    return "index.html"


@DynamicSetting
def ARTICLE_URL(metadata, *args, **kargv):
    return get_url(metadata)


@DynamicSetting
def ARTICLE_SAVE_AS(metadata, *args, **kargv):
    url = get_url(metadata)
    return url_to_file(url)


@DynamicSetting
def PAGE_URL(metadata, *args, **kargv):
    return get_url(metadata)


@DynamicSetting
def PAGE_SAVE_AS(metadata):
    url = get_url(metadata)
    return url_to_file(url)


ARTICLE_LANG_SAVE_AS = ARTICLE_SAVE_AS
ARTICLE_LANG_URL = ARTICLE_URL

#USE_FOLDER_AS_CATEGORY = True
#FILENAME_METADATA = '(?P<slug>.*)'
FILENAME_METADATA = '([^-]+-)?(?P<slug>.*)'
PATH_METADATA = '[^\/]+/(?P<category>[^/]+).*/([^-]+-)?(?P<slug>[^\.-]+)\.[^\.]+'

ARTICLE_ORDER_BY = 'source_path'
PAGE_ORDER_BY = 'source_path'

CONTENT_FILES = []
for path in PAGE_PATHS + ARTICLE_PATHS:
    for f in rcglob("content/"+path, "!md", "*"):
        if f.is_file():
            CONTENT_FILES.append(str(f).split("/", 1)[-1])

FAVICON_FILES = [i.split("/",1)[-1] for i in myglob("content/extra/favicon/*.",
    "png",
    "ico",
    "svg",
    "webmanifest",
    "xml"
)]

STATIC_PATHS = [
    'images',
    'extra/robots.txt'
] + FAVICON_FILES + CONTENT_FILES

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
for f in FAVICON_FILES:
    EXTRA_PATH_METADATA[f] = {'path': os.path.basename(f)}
for f in CONTENT_FILES:
    EXTRA_PATH_METADATA[f] = {'path': f.split("/", 1)[-1]}


THEME = cur_dir + '/themes/notmyidea-custom'
THEME = cur_dir + '/themes/mini'

REPLACEMENTS_CONFIG = cur_dir + "/config/replacements.yml"
PLUGINS = [reader, replacements, mod_content, mod_html, set_count, category_meta]

PUBLISH_ALL = True
