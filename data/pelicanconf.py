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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Location of the theme we are using
THEME = "theme"

DISPLAY_PAGES_ON_MENU = True

DELETE_OUTPUT_DIRECTORY = False

SOCIAL_ICONS_MENU = (
            ("Feed", "theme/images/feed.png", "feeds/all.atom.xml"),
            ("Contact", "theme/images/contact.png", "mailto:victor.gil.sepulveda@gmail.com"),
            ("Twitter", "theme/images/twitter.png", "https://twitter.com/intent/follow?screen_name=vgilsep"),
            ("LinkedIn", "theme/images/linked-in.png", "https://es.linkedin.com/in/víctor-a-gil-4509b0115"),
            ("Google+", "theme/images/google-plus.png", "https://plus.google.com/u/0/110041683601844851417"),
            )

PLUGINS = ['my_pelican_plugins.static_repo_generation','summary.summary',]

DIRECT_TEMPLATES = ['index', 
                    'categories', 
                    'authors', 
                    'archives', 
                    "repositories_static",
                    "tags", 
                    "cv"]
LINKS = (
        ("Home", "/"),
        ("Tags", "/tags.html"),
        ("Repos", "/repositories_static.html"),
        ("My CV", "/cv.html")
        )

STATIC_PATHS = [ # TODO : Robots.txt
    'images', 
    'extra/favicon.ico' ,
    'extra/CV.pdf',
    'extra/CNAME'
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CV.pdf' : {'path': 'CV.pdf'},
    'extra/CNAME' : {'path': 'CNAME'}

}

REPOS_DO_PROCESS = False
REPOS_DO_CHART = False
REPOS_GITHUB_USER = "victor-gil-sepulveda"
REPOS_BITBUCKET_USER = "victor_gil_sepulveda"

# not needed if using the summary plugin
#SUMMARY_MAX_LENGTH = 50
