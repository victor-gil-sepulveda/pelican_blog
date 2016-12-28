Downloading music from Youtube
##############################

:date: 2016-12-15 21:13
:tags: memory, Youtube, download, ffmpeg, parallel, pyScheduler, Python
:category:
:slug: downloading-music-from-youtube
:status: published


If you like music and Youtube is your main source, I am pretty sure that, at some point, you wanted to save some of the songs to disk. It is not impossible, indeed there are a million tools out there targeting this same problem. My personal choice has always been `JDownloader <http://jdownloader.org/>`_, but I must say this is not the best software you can find: it is heavy and it is very obscure.

.. PELICAN_BEGIN_SUMMARY

The last time I had to reinstall my OS (that is, two weeks ago) I decided to look for something lighter than JDownloader. After a not-so-long search I found `youtube-dl <http://rg3.github.io/youtube-dl/>`_, a very powerful command line video downloader for Youtube. 

.. PELICAN_END_SUMMARY

youtube-dl is great. It is really easy to use, and it works like a charm, but it downloads videos, not sound files. This means a bit of postprocessing is needed. Thanks to God I found an incredibly handy `post from Emre Sevinc in Linux Journal <http://www.linuxjournal.com/content/grabbing-your-music-youtube-do-it-your-way>`_. There, he explains how to postprocess the downloaded video using ffmpeg and lame, and also offers a bash script to automate the job (which I will not reproduce here, just go to the original article and C-c C-p !!). The script however has some flaws that may be caused by its age (the original post is from 2011!):

 - It expects youtube-dl to download only *flv* files, which is not true anymore.
 - The two-step conversion using ffmpeg and lame could have been handled in a more elegant way with a one-liner like :code:`ffmpeg -i [input] -vn -c:a libmp3lame [ouput].mp3`. However, this is a matter of taste.
 - It does not make the most of the newest flags youtube-dl has. And this one is crucial. 

A new script using Python
~~~~~~~~~~~~~~~~~~~~~~~~~
I must admit that my first impulse was to "fix" the bash script, but then I thought that maybe writing something similar would be quite easy in Python. And I did it. My final goal was to have something able to download the videos using a batch url file, and rename them if a new name was provided. The type of batch file I wanted to use was: 

.. code:: bash
	
	url1 rename to this
	url2 rename to that
	url3
	url4 rename again
	...  

The code can be download from in my Github repo (`here <https://github.com/victor-gil-sepulveda/YoutubeMusicDownloader>`_).

Youtube-dl new command line options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
As I already said youtube-dl comes with a lot of new functionalities. For instance, it is possible to ask only for the audio tracks and convert them, with something like this:

.. code:: bash
	
	> youtube-dl [url] -x --audio-format mp3 --audio-quality 0

That means: Download the music (-x) from [url], and convert it to mp3 (--audio-format mp3) with maximum possible quality (--audio-quality 0).

So, this does exactly what Emre Sevinc's bash script was doing, converting it automatically in a redundant piece of software.

Also, it is possible to use a batch file to provide urls. This batch file has the form:

.. code:: bash

	url1
	url2
	...
	urln

And with a line like this one: 

.. code:: bash

	> youtube-dl -a [batch file] -x --audio-format mp3 --audio-quality 0

youtube-dl will download the music of all urls. This does exactly the same than my script (except for the renaming). Even the batch files can be used interchangeably. And this makes my 100 lines script redundant too. Or not?

Parallelization
~~~~~~~~~~~~~~~

The batch mode of youtube-dl has only one minor problem (imho), it treats each url in a serial fashion. This looks like the kind of problems where task-level parallelization could improve the overall performance a lot. To this end I used `pyScheduler <https://github.com/victor-gil-sepulveda/pyScheduler>`_ . The changes were minimum:

 - Detect and extract the task to a function
 - Create a scheduler and add the tasks

The results are pretty good when compared with youtube-dl batch mode. I have tested the script using a batch file of small videos (with a lot of versions of the beautiful "Moon River") and another one that includes longer videos. Downloading them using youtube-dl's batch mode took an average of around 89s. My parallelized script was faster in all cases when using more than one process. It is worth to mention that pyScheduler uses one process as a master controller, so the "real" number of processes used is always n-1. That is why, when the script detects an n <= 2, it defaults to the serial scheduler, which is more efficient. 

The average results for the "small batch" are shown in the plot below (times averaged over 10 runs, except in the last case, where I did only 5 runs).
  
.. image:: {filename}/images/2016_12_15_downloading-music-from-youtube__small_time.png
	:width: 600 px
   	:alt: Plot 1

As you can see, the serial behaviour (for n = 2, n = 1 was omitted) is very similar (speedup around *1x*). The maximum speedups is obtained with 6 processes (*1.8x*), but it is obvious that increasing the number of processes above 5 does not throw better results. The performance decreases slightly when using 7 processes, which may be related with the fact that my CPU has only 6 cores (I had to try ^.^u ).  Indeed the most noticeable gain is obtained using only 3 processes (2 worker processes). 

When trying to download more and larger videos the behaviour looks like this:

.. image:: {filename}/images/2016_12_15_downloading-music-from-youtube__big_time.png
	:width: 600 px
   	:alt: Plot 2

The test was averaged over a minimum of 3 runs (an outlier for n=6 was removed). The plot shows that, again, the maximum performance change is obtained with n=3 (2 "real processes"). Given that youtube-dl took around 711s to download the files, the speedup for n=3 is already a not-that-bad *1.3x*.

Final words
~~~~~~~~~~~
Youtube-dl is an incredibly complete tool to download audio and videos from Youtube. Its batch mode open the doors to really naughty uses like audio scrapping (for research purposes, of course).

The parallelization of my batch script looks to have had an interesting outcome. A small number of processes can increase the performance almost *1.5x*, which is not that bad. The script could be improved, of course. It would be interesting to avoid overlapping ffmpeg conversions (it may use more than one core and produce a bottleneck) and to improve the load balance. Of course, this would mean to have finer control over youtube-dl, and also to code some more hundred lines of code. 

Remember that musicians are not photosynthetic (yet) and they need your money to live. If you like their music, consider contributing with their work by buying original discs and going to their concerts.

But, anyway, the next time you feel the urge of downloading some music from Youtube, just stay apart from all those über-complex contraptions hanging around. Use the command line!

Take care!

   

