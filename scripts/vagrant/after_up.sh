#!/usr/bin/env bash

DIRECTORY="blog"

# delete everything under blog
if [ -d "$DIRECTORY" ]; then
  rm -rf $DIRECTORY
fi

# Start fresh Pelican blog
python /vagrant/pelican/auto_quickstart.py
ln -s /vagrant/contents ./blog/contents
