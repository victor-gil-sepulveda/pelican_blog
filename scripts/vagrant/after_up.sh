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

# CV page files
ln -s /vagrant/data/cv/cv.html /home/vagrant/blog/theme/templates/cv.html
ln -s /vagrant/data/cv/images/self_portrait.jpg /home/vagrant/blog/theme/static/images/self_portrait.jpg
ln -s /vagrant/data/cv/images/pdf-file.jpg /home/vagrant/blog/theme/static/images/pdf-file.jpg

# Repositories page files
ln -s /vagrant/data/repositories/repositories.html /home/vagrant/blog/theme/templates/repositories.html
ln -s /vagrant/data/repositories/repositories_static.html /home/vagrant/blog/theme/templates/repositories_static.html
ln -s /vagrant/data/repositories/js/github_repos.js /home/vagrant/blog/theme/static/js/github_repos.html
ln -s /vagrant/data/repositories/images/bitbucket.png /home/vagrant/blog/theme/static/images/bitbucket.png
ln -s /vagrant/data/repositories/images/github.png /home/vagrant/blog/theme/static/images/github.png

# Handle extra folder (favicon, robots etc)
if [ ! -d /home/vagrant/blog/content/extra ]; then
    echo "Adding extra data dir ..."
    ln -s /vagrant/data/extra /home/vagrant/blog/content/extra
fi

EOF

