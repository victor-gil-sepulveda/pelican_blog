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

LINKS = (
        ("Home", "/"),
        )

DISQUS_SITENAME = "thelostlibraryofagraphur"
