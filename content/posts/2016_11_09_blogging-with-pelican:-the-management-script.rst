Blogging with Pelican: The Management Script
############################################

:date: 2016-11-9 11:06
:tags:
:category:
:slug: blogging-with-pelican:-the-management-script
:status: published

.. PELICAN_BEGIN_SUMMARY

At some point, when you start to do serious blogging, automation is needed. To be honest, this is not my case right now (I just wrote three posts so far in my new blog incarnation, which does not look too serious), but it is always fun to try new things.

.. PELICAN_END_SUMMARY

The main goal here is to create a Python script that helps us performing some common operations that can be identified as part of the blogging work flow, like:

- Creating new empty pages and posts (*new\_page*, *new\_post*)

- Starting the development web server (*serve*)

- Cleaning the symlink structure (*remove\_symlinks*)

- Publishing changes to Github (*publish*)

For the command line interface parsing, I wanted to try `clip.py <https://github.com/willyg302/clip.py>`_ as an alternative to the well-known *optparse* module. This tiny package allows to define the commands, arguments and options of your script in a declarative way by using Python decorators.

You can find the complete script `here <https://github.com/victor-gil-sepulveda/victor-gil-sepulveda.github.io/blob/source/scripts/local/manage.py>`_.

Creating new empty pages and posts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The idea (and part of the code) comes from `this page <http://nafiulis.me/making-a-static-blog-with-pelican.html>`_. Basically, this command uses two reStructured Text templates, one for the `pages <https://github.com/victor-gil-sepulveda/victor-gil-sepulveda.github.io/blob/source/scripts/local/new_page.template>`_ and other for the `posts <https://github.com/victor-gil-sepulveda/victor-gil-sepulveda.github.io/blob/source/scripts/local/new_post.template>`_, and populates the title, date etc. with proper values. Then it writes them to the /content/pages or content/posts folders. This is exactly the same that Octopress did, but with less magic.


Starting the development web server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
I also needed a way to perform quick tests with the new posts. This involves to start the VM and start the development server. In order to manage the VM with vagrant from the script I use the handy `python-vagrant <https://github.com/todddeluca/python-vagrant>`__ Python module. Once the VM is up, the script calls an inner VM bash script through an ssh command. 

The problem with the development server is that it cannot recover from errors. If an error happens, one has to enter the VM, kill the process and restart the server (if needed). 
 
This command does not automatically stop the VM.


Cleaning the symlink structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A script is executed whenever a vagrant up event happens, in order to recreate the blog workspace. This generates tones of symbolic links in the host, that can become burden if using *git* for version control, as it treats links as regular files. Before issuing a git status command, it is convenient to remove this symbolic links.  


Publishing changes to Github 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Every time I want to publish the changes I have to start the virtual machine, generate the publish version of the blog and upload it to the repository. The script starts the VM using `python-vagrant <https://github.com/todddeluca/python-vagrant>`__, then it issues an ssh command that runs a script in the host. This script  is in charge of generating the files and moving the results to the shared folder. Finally it uses `ghp-import <https://github.com/davisp/ghp-import>`_ to move the newly created files to the master branch of the repository in Github Pages so that they get published.

Again, the script does not stop the VM, so in case halting the VM it is needed, it must be done manually. 

Adding simple bash completion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
It is very cool to have a script that allows you to automate tasks, but it is even cooler if you do not have to write too much in order to use it. That is why I tried to add a simple autocompletion feature to the script.

I have investigated how this kind of autocompletion could be done with Python and ... well ... it looks like it cannot be done. At least directly. But it is quite easy to add 1st level autocompletion to a Bash script. The solution is then to create a Bash script wrapper for the Python script. Unnecessarily complex? yes, but this is another of these things I just do for the sake of learning. 

`This page <https://www.gnu.org/software/bash/manual/bashref.html#Programmable-Completion-Builtins>`__ explains how to use the autocompletion mechanisms of Bash. Basically, one has to register the words to be used for autocompletion by adding this line to your *.bashrc* file:

.. code-block:: bash

    complete -W "new_page new_post publish remove_symlinks serve" blog_manage   

Obviously the *blog_manage* bash script is already in our PATH.

Take care!


