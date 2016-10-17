#!/usr/bin/env bash

vagrant plugin install vagrant-triggers

git clone https://github.com/willyg302/clip.py.git
cd clip.py/
sudo python setup.py install
cd ..

sudo pip install python-vagrant

sudo apt install ghp-import


# for the blog_manage script
# TODO: Try adding the py script to the PYPATH
# ADD bin folder to PATH
# THEN REGISTER BY ADDING THIS TO BASHRC (UPDATE OPTIONS WHEN NEEDED)
complete -W "new_page new_post publish remove_symlinks serve" blog_manage
