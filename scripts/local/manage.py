import os, inspect, clip
from datetime import datetime
import vagrant

def load_template(name):
    current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return open(os.path.join(current_path,name)).read()


app = clip.App()

@app.main(description='Basic manager for my Pelican Blog')
def manage():
    pass

@manage.subcommand(description='Starts the development server')
def serve():
    vagrant_handler = vagrant.Vagrant()
    if vagrant_handler.status()[0].state != "running":
        vagrant_handler.up()
    os.system('vagrant ssh -c "bash /vagrant/scripts/vagrant/start_serving.sh"')

@manage.subcommand(description='Creates a new post using the current timestamp')
@clip.arg('title', required=True, help='The title of the post')
@clip.flag('-d', '--draft', help='If defined, the new post will be a draft')
def new_post(title, draft):
    """
    Based on http://nafiulis.me/making-a-static-blog-with-pelican.html
    """
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    os.system("mkdir -p content/posts")
    f_create = "content/posts/{}_{:0>2}_{:0>2}_{}.rst".format(
        today.year, today.month, today.day, slug)
    t = load_template("new_post.template").format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug,
                                draft = "draft" if draft else "published")
    with open(f_create, 'w') as w:
        w.write(t)
    clip.echo('File created -> {}'.format(f_create))

@manage.subcommand(description='Creates a new page')
@clip.arg('title', required=True, help='The title of the post')
@clip.opt('-a', '--author', default=u"V0x0237ctor Gil", help='Author of the page')
@clip.opt('-s', '--summary', default="", help='Brief explanation of page contents')
def new_page(title, author, summary):
    today = datetime.today()
    os.system("mkdir -p content/pages")
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/pages/{}.rst".format(slug)
    t = load_template("new_page.template").format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug,
                                author = author,
                                summary = summary)
    with open(f_create, 'w') as w:
        w.write(t)
    clip.echo('Page created -> {}'.format(f_create))


@manage.subcommand(description='Removes symlinks')
def remove_symlinks():
    os.system("find -type l -delete")

@manage.subcommand(description='Publishes the blog to github pages. Errors are not handled.')
@clip.flag('-v', '--verbose', help='Verbose flag')
def publish(verbose):
    OUT_DIR = "ghp-output"

    # Clean up the directory if it exists
    command = "if [ -d %s ]; then rm -rf %s; fi;"%(OUT_DIR, OUT_DIR)
    #os.system(command)
    if verbose: print command

    # This is run in the vm system and copy everything to the shared folder;
    # Symlinks are converted to their copied counterparts
    command = "vagrant ssh -c '/vagrant/scripts/vagrant/publish.sh %s %s'"%(OUT_DIR, "-v" if verbose else "")
    #os.system(command)
    if verbose: print command

    # Then ghp-import is used to publish it (to the master branch).
    # It needs a repo to be set up (in this case already set up to my gh pages repo.
    # Last versions have the -f (force) flag for the push command 
    command = "ghp-import -b master -p -m 'New blog update' %s "%OUT_DIR
    os.system(command)
    if verbose: print command

if __name__ == '__main__':
    try:
        app.run()
    except clip.ClipExit:
        pass
