#!/usr/bin/env bash

# In order to work as vagrant user 
# we need this hack
sudo -u vagrant -H bash << EOF
# Delete everything under blog
if [ -d /home/vagrant/blog ]; then
  echo "Deleting blog folder..."
  rm -rf /home/vagrant/blog
fi

# Regenerates Pelican blog
python /vagrant/scripts/vagrant/auto_quickstart.py
rm -rf blog/content

# Link the folder inside the shared folder where
# we are going to add the blog pages and posts
ln -s /vagrant/content /home/vagrant/blog/content
ln -s /vagrant/data/theme /home/vagrant/blog/theme
rm /home/vagrant/blog/pelicanconf.py
ln -s /vagrant/data/pelicanconf.py /home/vagrant/blog/pelicanconf.py

# Handle extra folder (favicon, robots etc)
if [ ! -d /home/vagrant/blog/content/extra ]; then
    echo "Adding extra data dir ..."
    ln -s /vagrant/data/extra /home/vagrant/blog/content/extra
fi

EOF

