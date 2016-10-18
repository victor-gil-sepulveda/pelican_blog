#!/usr/bin/env bash

#sudo apt-get update
sudo apt-get install -y python-dev
sudo apt-get install -y python-pip

pip install pelican
#pip install fabric
pip install ghp-import
pip install pexpect # Must issue a Python3 related error. Not relevant for this installation.

pip install livereload

echo "export PYTHONPATH=/vagrant/plugins:/vagrant/plugins/pelican-plugins:\$PYTHONPATH" >> /home/vagrant/.bashrc
