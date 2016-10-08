#!/usr/bin/env bash


DIRECTORY="blog"

# In order to work as vagrant user 
# we need this hack
sudo -u vagrant -H bash << EOF

# delete everything under blog
if [ -d "$DIRECTORY" ]; then
  rm -rf $DIRECTORY
fi

# Regenerates Pelican blog
python /vagrant/scripts/vagrant/auto_quickstart.py
rm -rf blog/content
# Link the folder inside the shared folder where
# we are going to add the blog pages and posts
ln -s /vagrant/content ./blog/content

EOF
