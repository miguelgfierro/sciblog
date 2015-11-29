A blog with the appearance of a scientific Latex paper.
==================

We need to install several libraries:

	$ apt-get install -y python-dev libpq-dev python-pip git apache2 libapache2-mod-wsgi
	$ pip install django django-debug-toolbar markdown2

NOTE: django version must be 1.7 or 1.8. To see your django version:

	$ pip list

Install the project
==================================================
The first step is to generate the database. In the projects folder:
  
	$ python manage.py syncdb  
Django will ask you to create a superuser. You have to put the username and password. The email is optional. 
This will generate a file called db.sqlite3 which is the database where all the blog content is stored.

After that you have to make what is called a migration, to create the tables in your database. To do that:
	
	$ python manage.py makemigrations
	$ python manage.py migrate

In another terminal you have to run django server:

	$ python manage.py runserver  
	
In a browser put the link: http://localhost:8000/admin/

To run the django server in a server VPS with IP:111.111.111.111

	$ python manage.py runserver 111.111.111.111:8000 

In a browser put the link: http://111.111.111.111:8000/admin/

The panel will ask you to put username and password. Once you are in django dashboard you can start to add content to
your blog.

Add your first content to the blog
==================================================

Press add in Post to add your first post. Go to file latex_blog.txt and start to fill up all the fields. For the first
post we will leave the image, the image caption, page 2 column 1 and page 2 column 2 empty.

You will see that your blog is working properly going to the url: http://localhost:8000/blog/ (note: make sure you put the slash at the end)

The post can be accessed here: http://localhost:8000/blog/2015/a-blog-with-the-appearance-of-a-scientific-paper-in-latex/

Now take the file prince_ali.txt and add a second post. This time you'll have to fill all fields. The image you have to use
is in img/prince_ali.jpg



