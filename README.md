A blog with the appearance of a scientific Latex paper.
==================

We need to install django, django-toolbelt and South:

	$ apt-get install -y libpq-dev python-dev
	$ pip install django django-toolbelt south

NOTE: django version must be less than 1.7. To see your django version:

	$ pip list
To downgrade your django version:
	$ pip install -U "django<1.7"