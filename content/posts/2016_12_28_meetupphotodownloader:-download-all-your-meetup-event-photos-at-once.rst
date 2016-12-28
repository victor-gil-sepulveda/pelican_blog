Meetup Photo Downloader: download all your Meetup event photos at once
######################################################################

:date: 2016-12-28 9:54
:tags:
:category:
:slug: meetupphotodownloader:-download-all-your-meetup-event-photos-at-once
:status: published



.. PELICAN_BEGIN_SUMMARY

Recently I rediscovered `Meetup <https://www.meetup.com>`_. It is a web platform where people can propose and join events that range from tech talks to mountain hikes. It offers tools to contact the people, organizing the event and, eventually, to upload photos. Users can upload groups of photos in a very convenient way, but the problem comes when another user wants to download them: she has to download them one by one. I have been there: it is quite tedious.

.. PELICAN_END_SUMMARY

The goal of this project was to create a **static web application** that automates the downloading of all the photos related to a Meetup event. The idea is that the user selects a group and the event he is interested in, and then the web app downloads all the photos in a nicely packed in a zip file. As easy as that!

The Meetup Photo Downloader has been uploaded `here <http://www.thelostlib.com/MeetupPhotoDownloader/>`__. The code has been released under MIT license, and can be found `here <https://github.com/victor-gil-sepulveda/MeetupPhotoDownloader>`_.


Technologies and methods used
-----------------------------
Jquery
******
Even if there are other alternatives for HTML manipulation, this is the one I am more comfortable with. I did not learn new things about it, but it is always useful to remember!  

Meetup REST API
***************
In order to get the user data from Meetup I have used their `API <https://www.meetup.com/es-ES/meetup_api/>`_. Whatever you can do with their platform you can do it with their API. Using their endpoints is not trivial, but after reviewing their documentation a couple of times, and going through the examples, it becomes doable.

The API cannot be used without being an valid Meetup user, that is why the first thing the app needs to login into meetup in order to get a session key. This is achieved by redirecting to a login URL, which, after the login, will redirect again to the return page you have specified. The redirected url will contain the needed session data, and has to be parsed.

The scheme to use the other API calls is easier. One just needs to connect to the endpoint and GET the JSON data. I just used two of them, one to obtain the group and event information, and the other to retrieve the photos for a given event.  

Image downloading 
*****************
Downloading an image from a server in a different domain can be a pain in the ass. Period. Thanks to God I am not the first one having this issue. Henry Algus shows `here <http://www.henryalgus.com/reading-binary-files-using-jquery-ajax/>`__ a suitable way to address this problem, along with a JQuery plugin.

The code needed to download a photo becomes:

.. code:: javascript

	$.ajax({
		    url: [--URL--],
		    type: "GET",
		    crossDomain: true,
		    xhrFields: {cors: false},
		    dataType: 'binary',
		    processData: false
	})
	.done(...)
	.fail(...)

Responsive design
*****************
I also wanted to experiment with responsive design, i.e. a design that changes as the screen size varies. 

For the layout I used `skeleton.js <http://getskeleton.com/>`_, more specifically, its grid feature. Skeleton allows the designer to define grids and rows that will stack gracefully when the viewport size decreases.

For the responsive image header I used the <picture> tag. I decided that I wanted to try with an svg image first. If the browser cannot render *svg*, the fallback is a set of png images of decreasing size, each associated with a different range of viewport sizes.

.. code:: html

	<picture>
		<source type="image/svg+xml" srcset="img/meetup.svg">
		<source srcset="img/header.big.png" media="(min-width: 1000px)">
		<source srcset="img/header.med.png" media="(min-width: 540px)">
		<source srcset="img/header.sma.png" media="(min-width: 0px)">

		<img src="img/header.med.png"
		    alt="Meetup Photo Downloader"
		    style="width:100%;margin-bottom:40px;margin-top:40px;"
		>
	</picture>


Unit testing
************
I must admit this was one of the things I was most interested into, as I had never used a unit testing approach before with Javascript. For the unit testing I used Node + Mocha + Chai ( `this site <http://nodeguide.com/beginner.html>`_ gives a good explanation on how to use both).

"Callback hell"
***************
I made extensive use of promises and arrays of promises where possible. Again, this is another feature I had never used until now.

Advertisements
**************
And finally, another thing I never did. I was just curious about how adding adds to a web page felt. I tried with Google adSense, but they did not accept me. Then I tried with Chitika. The experience has been good so far.

One of the biggest problems I found was choosing where to place the add banner, specially because it disrupts the design of the page. 

Criticism
---------
As with all the other projects I have been coding lately, I did this one for the sake of learning. This means I put more care into some parts \.\.\. and less or nothing in some other aspects.

One of the things I am less proud off are the modal dialog. In the past I used `JQuery UI <https://jqueryui.com/>`_ for this, but this time I wanted to do something from scratch. The result really needs some improvement. 

The markup is full of inline styles (yuck!) which also break the "responsiveness" of the design.

I should do a bigger effort into separating the MVC components... and tidy up the main.js file a bit. It is really messy.

Finally, in my opinion the most urgent improvements would be to localize the text to more languages (for instance using `l10n <https://github.com/eligrey/l10n.js/>`_, to test the remaining parts with a headless browser and to polish the overall design and error handling.

I hope the app fits your needs. If not, use the comments to suggest new improvements!!

