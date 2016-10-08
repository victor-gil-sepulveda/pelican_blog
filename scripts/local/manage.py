import os, inspect, clip
from datetime import datetime

def load_template(name):
    current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return open(os.path.join(current_path,name)).read()


app = clip.App()

@app.main(description='Basic manager for my Pelican Blog')
def manage():
    pass

@manage.subcommand(description='Creates a new post using the current timestamp')
@clip.arg('title', required=True)
@clip.opt('-d', '--draft', default=True, help='If defined, the new post will be a draft')
def make_entry(title, draft):
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

if __name__ == '__main__':
    try:
        app.run()
    except clip.ClipExit:
        pass
