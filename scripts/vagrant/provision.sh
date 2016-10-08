#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install expect
pip install pelican
pip install fabric
pip install ghp-import

mkdir blog
python /pelican/scripts/auto_quickstart.py
ln -s /vagrant/contents blog/contents
