import pexpect
child = pexpect.spawn ('pelican-quickstart')

child.expect ('new web site?', timeout=5)
child.sendline('blog')

child.expect ('be the title of this web site?', timeout=5)
child.sendline('The lost library of Agraphur')

child.expect ('the author of this web site?', timeout=5)
child.sendline('Victor A. Gil')

child.expect ('language of this web site?', timeout=5)
child.sendline('en')

child.expect ('want to specify a URL prefix?', timeout=5)
child.sendline('N')

child.expect ('enable article pagination?', timeout=5)
child.sendline('Y')

child.expect ('articles per page do you want?', timeout=5)
child.sendline('10')

child.expect ('time zone?', timeout=5)
child.sendline('Europe/Paris')

child.expect ('generate a Fabfile/Makefile to automate generation and publishing?', timeout=5)
child.sendline('Y')

child.expect ('auto-reload & simpleHTTP script to assist with theme and site development?', timeout=5)
child.sendline('Y')

child.expect ('upload your website using FTP?', timeout=5)
child.sendline('N')

child.expect ('upload your website using SSH?', timeout=5)
child.sendline('N')

child.expect ('upload your website using Dropbox?', timeout=5)
child.sendline('N')

child.expect ('upload your website using S3?', timeout=5)
child.sendline('N')

child.expect ('upload your website using Rackspace Cloud Files?', timeout=5)
child.sendline('N')

child.expect ('upload your website using GitHub Pages?', timeout=5)
child.sendline('Y')

child.expect ('your personal page', timeout=5)
child.sendline('Y')

child.expect(pexpect.EOF)
