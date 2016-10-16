#!/usr/bin/env bash

vagrant plugin install vagrant-triggers

git clone https://github.com/willyg302/clip.py.git
cd clip.py/
sudo python setup.py install
cd ..

sudo pip install python-vagrant

sudo apt install ghp-import