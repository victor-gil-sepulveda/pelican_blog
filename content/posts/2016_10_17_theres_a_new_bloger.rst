Blogging with Pelican: First Impressions
########################################

:date: 2016-10-17 19:30
:tags: Pelican, 
:category:
:slug: theres_a_new_bloger
:status: published


There's a new blogger in town!
------------------------------

It was the year 2014. I was young and inexperienced [1]_, and I wanted to start a web log. At that time I was coursing a PhD, which is a well known way of being poor for the rest of your life [2]_, reason why I looked for a free hosting solution where my (obviously static) blog would reside. The winner from my not-so-impressive list was Github pages.  

Github pages can process Jekyll_ blogs out of the box, which looked like a very fancy feature, but Jekyll did not look so fancy to me. It was written in Ruby and I did not had patience to learn that language. But there was still another option: Octopress_. They were claiming that it was a very automatized Jekyll blog generation tool. I believed it. And this was my first and last mistake as blogger.

My experience with Octopress
----------------------------

As you may have already guessed from the previous paragraph, my experience with Octopress was not that good. First and foremost, all the magic it was performing made me feel uncomfortable. But maube the most important thing is that it was cluttering my blog workspace with tones of folders and configuration files. And as I did not read the code, I did not have any clue of how the generation process worked.  

In more than two years I only published a post. And its source file just disappeared one of those times I had to reinstall Octopress. I also wrote a lot of other proto-posts in *txt* files. All were lost the last time I had to change the *OS*. So, in conclusion, Octopress was not fostering my productivity at all.

Long live Pelican!
------------------
Recently, and thanks to several conversations with professional recruiters, I have discovered that my CV is too difficult to understand. It is understandable: since they receive tones of CVs per day and only have some minutes to spend with every one, a too complex CV is the first step to failure. Besides, my CV has two added handicaps: first,  it is an "academic CV", which means it is long and full of details that are of no interest to regular companies. Second, I have worked as a `Research Software Engineer <http://www.rse.ac.uk/who.html>`_ these last 9 years, which is a rare and difficult to explain role. This meant I had to devise a better way to present myself to prospective employers. What about trying with a blog again? Why not?

Again, I focused on static blog generators, but this time I decided I wanted it to be in a language I already mastered: Python. There are many choices (ej. Nikola_, Hyde_), and I just picked the one that looked to have the smaller codebase: Pelican_.  

.. PELICAN_BEGIN_SUMMARY  

Starting a blog with Pelican is incredibly easy. Just use the "quickstart" script and download a theme. You will have a complete blog in a matter of minutes. And, also very important, you will not end with cluttered workspace: in its simplest form, Pelican just needs a contents folder and a couple of configuration scripts. Which are written in Python too. Delightful.

.. PELICAN_END_SUMMARY  

There are only two drawbacks of Pelican as far as I have seen:

- The documentation is too brief and does not cover all the features in detail. It can become very difficult to obtain information about how to extend Pelican with plugins or about how to use some configuration options (which can give you the impression that some of them are buggy). You will end learning by example, thanks to the several other Pelican users that have documented their efforts.  

- It does not have a managing system for simple and repetitive tasks like creating posts, which other static generators like Octopress have.

I suppose the first issue will improve over time, and about the second one ... well, you can do it yourself. At the end of the day that is  

.. [1] Now I am older and yet inexperienced.
.. [2] You gain extra poverty points if you do it in Spain!
.. _Nikola: https://getnikola.com/
.. _Hyde: http://hyde.github.io/
.. _Pelican: http://blog.getpelican.com/
.. _Octopress: http://octopress.org/ 
.. _Jekyll: https://jekyllrb.com/
