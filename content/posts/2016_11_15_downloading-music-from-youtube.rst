Downloading music from Youtube
##############################

:date: 2016-12-15 21:13
:tags: memory, Youtube, download, ffmpeg
:category:
:slug: downloading-music-from-youtube
:status: published


If you like music and Youtube is your main source, I am pretty sure that, at some point, you wanted to save some of the songs to disk. It is not impossible, indeed there are a million tools out there targeting this same problem. My personal choice has always been `JDownloader <http://jdownloader.org/>`_, but I must say this is not the best software you can find: it is heavy and it is very obscure.

.. PELICAN_BEGIN_SUMMARY

The last time I had to reinstall my OS (that is, two weeks ago) I decided to look for something lighter than JDownloader. After a not-so-long search I found `youtube-dl <http://rg3.github.io/youtube-dl/>`_, a very powerful command line video downloader for Youtube. 

.. PELICAN_END_SUMMARY

youtube-dl is great. It is really easy to use, and it works like a charm, but it downloads videos, not sound files. This means a bit of postprocessing is needed. Thanks to God I found an incredibly handy `post from Emre Sevinc in Linux Journal <http://www.linuxjournal.com/content/grabbing-your-music-youtube-do-it-your-way>`_. Here, he explains how to postprocess the downloaded video using ffmpeg and also offers a bash script to automate the job (which I will not reproduce here, just go to the original article and C-c C-p !!). 

So, the next time you feel the urge of downloading some music from Youtube, just stay apart from all those über-complex contraptions hanging around. Use the command line!

   

