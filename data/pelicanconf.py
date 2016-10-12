#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Víctor A. Gil'
SITENAME = u'The lost library of Agraphur'
SITESUBTITLE = u'Pieces from a whole'
SITEURL = '' # for correct feed generation

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (,)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Location of the theme we are using
THEME = "theme"

DISPLAY_PAGES_ON_MENU = True

DELETE_OUTPUT_DIRECTORY = False

SOCIAL_ICONS_MENU = (
            ("Feed", "theme/images/feed.png", ""),
            ("Contact", "theme/images/contact.png", ""),
            ("Twitter", "theme/images/twitter.png", ""),
            ("LinkedIn", "theme/images/linked-in.png", ""),
            ("Google+", "theme/images/google-plus.png", ""),
            )

PLUGINS = ['my_pelican_plugins.static_repo_generation',]
GITHUB_USER = "victor-gil-sepulveda"
BITBUCKET_USER = "victor_gil_sepulveda"
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', "repositories_static", "tags"]
LINKS = (
        ("Home", "/"),
        ("Tags", "/tags.html"),
        ("Repos", "/repositories_static.html")
        )

DISQUS_SITENAME = "thelostlibraryofagraphur"

STATIC_PATHS = [ # TODO : Robots.txt
    'images', 
    'extra/favicon.ico' 
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

#TEMPLATE_PAGES = {'theme/repositories_static.html': 'repositories.html'}

