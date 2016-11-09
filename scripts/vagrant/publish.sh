#!/usr/bin/env bash

cd /home/vagrant/blog

# TODO: Discover why this line is needed if it is already declared
# in the .bashrc file
export PYTHONPATH=/vagrant/plugins:/vagrant/plugins/pelican-plugins:$PYTHONPATH

#make publish
pelican -q -o ghp-output -s publishconf.py --ignore-cache

rsync ghp-output/ /vagrant/$1/ -a --copy-links $2
