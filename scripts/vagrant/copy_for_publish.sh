#!/usr/bin/env bash

cd /home/vagrant/blog

# TODO: Discover why this line is needed if it is already declared
# in the .bashrc file
export PYTHONPATH=/vagrant/plugins:$PYTHONPATH

#make publish
rsync output/ /vagrant/$1/ -a --copy-links $2