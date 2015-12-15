Sciblog: A blog with the appearance of a scientific Latex paper.
==================

Blog developed in django with the same appearance of a research paper written in Latex.

* CSS and Latex fonts integrated
* Add posts in two columns like a paper
* Add formulas with latex notation ( formulas between $ $ for inline and between $$ $$ for new line)
* Share in social networks
* RSS feed
* Post search 
* Blog optimized for SEO

Installation
==================

We need to install several libraries:

	$ apt-get install -y python-dev libpq-dev python-pip git apache2 libapache2-mod-wsgi
	$ pip install django django-debug-toolbar markdown2

NOTE: django version must be 1.7 or 1.8. 

Set up the project in localhost
==================================================
The first step is to generate the database. In the projects folder:
  
	$ python manage.py syncdb  
Django will ask you to create a superuser. You have to put the username and password. The email is optional. 
This will generate a file called db.sqlite3 which is the database where all the blog content is stored.

After that you have to make what is called a migration, to create the tables in your database. To do that:
	
	$ python manage.py makemigrations
	$ python manage.py migrate

In another terminal you have to run django development server:

	$ python manage.py runserver  
	
In a browser put the link: http://localhost:8000/admin/

The panel will ask you to put username and password. Once you are in django dashboard you can start to add content to
your blog.

When you are in localhost you have to set DEBUG = True in sciblog/settings.py. You can set it to False but you won't see the images the user uploaded through the admin dashboard. In production this is handled by apache.

Set up the project in a Ubuntu VPS server
==================================================

First make sure that you have installed git, apache2 and libapache2-mod-wsgi as explained before. 

	$ cd /var/www
	$ git clone https://github.com/hoaphumanoid/sciblog.git
	$ cd sciblog
	$ python manage.py syncdb  
	$ python manage.py makemigrations
	$ python manage.py migrate

Set the correct permissions:

	$ chown www-data:www-data /var/www/sciblog
	$ chown www-data:www-data /var/www/sciblog/db.sqlite3
	$ chown www-data:www-data /var/www/sciblog/img	

Configure apache (in sciblog.conf change miguelgfierro.com for your url):

	$ cp sciblog.conf /etc/apache2/sites-available/
	$ a2ensite sciblog.conf
	$ a2enmod rewrite
	$ a2enmod expires
	$ service apache2 restart
	
Add your first content to the blog
==================================================

Press add in Post to add your first post. Go to file content/latex_blog.txt and start to fill up all the fields. For the first
post we will leave the image, the image caption, page 2 column 1 and page 2 column 2 empty.

You will see that your blog is working properly going to the url: localhost:8000 (in production you'll have to add something like miguelgfierro.com without http://)

The post can be accessed here: http://localhost:8000/blog/2015/a-blog-with-the-appearance-of-a-scientific-paper-in-latex/

Now take the file content/prince_ali.txt and add a second post. This time you'll have to fill all fields. The image you have to use
is in img/prince_ali.jpg

Create the about page
==================================================

Go to the admin console and add your first flat page. A flat page is a static html code. 

In Flat pages press add. In url put /about/ (don't forget / in both sides). In title put your name, in sites put your site and in content paste the file content/about.txt. It will render a beautifull about page. 

Notes to manage the blog in the production environment
==================================================

When you are in production you have to set DEBUG = False in sciblog/settings.py.

Also the first time you enter in your admin console (http://miguelgfierro.com/admin/) you have to go to sites and EDIT the default site, which is example.com. Change it for the name of your site without http:// (my case would be miguelgfierro.com).
This will set the first entry in the database to your site, which is related to the variable SITE_ID = 1 in sciblog/settings.py. You can see the number of the site in http://miguelgfierro.com/admin/sites/site/1/. If you add another site then it will have a different number in the database, so for everything to work you have to change the variable SITE_ID. In my experience it is better if you don't touch anything, I messed up the database several times :-)



