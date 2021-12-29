[![Issues](https://img.shields.io/github/issues/miguelgfierro/sciblog.svg)](https://github.com/miguelgfierro/sciblog/issues)
[![Latest release](https://img.shields.io/github/release/miguelgfierro/sciblog.svg)](https://github.com/miguelgfierro/sciblog/releases)
[![Commits since latest release](https://img.shields.io/github/commits-since/miguelgfierro/sciblog/latest.svg)](https://github.com/miguelgfierro/sciblog/releases)
[![Twitter](https://img.shields.io/twitter/follow/miguelgfierro?style=social)](https://twitter.com/intent/follow?screen_name=miguelgfierro)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=social)](https://www.linkedin.com/in/miguelgfierro/)

# Sciblog: A blog with the appearance of a scientific paper

Blog developed in django with the same appearance of a research paper written in [Latex](https://en.wikipedia.org/wiki/LaTeX).

* CSS and Latex fonts integrated
* Posts are presented in two columns like a paper
* Formulas can be added with Latex notation
* Share in social networks
* RSS feed
* Post search
* Blog optimized for SEO
* Comments with disqus
* Easy writing with Ckeditor
* Responsive for mobile
* (Optional) Web optimization with CloudFlare
* (Optional) Installation of free SSL certificate
* (Optional) Privacy policy compliant with GDPR

Example of sciblog: [https://miguelgfierro.com](https://miguelgfierro.com)

<p align="center">
	<img src="img/blog_view.png" alt="blog view" width="45%"/>
	<img src="img/blog_view2.png" alt="blog view" width="45%"/>
</p>

## Installation

We need to install several libraries. In Linux the commands are:

	$ git clone https://github.com/miguelgfierro/sciblog.git
	$ apt-get install -y python-dev libpq-dev python-pip git apache2 libapache2-mod-wsgi build-essential
	$ pip install -r requirements.txt 

*NOTE: Django version must be 1.8, Apache at least 2.4.23 and Python 2.7.*

## Set up the project in localhost

The first step is to generate the database. In the project folder:
  
	$ cp sciblog/private.template.py sciblog/private.py
	$ python manage.py syncdb  

When you are in localhost you have to set `DEBUG = True` in `sciblog/private.py`. You can set it to `False` but you won't see the images the user uploaded through the admin dashboard. In production, this is handled by apache. You should also change `SECRETKEY`.

Django will ask you to create a superuser. You have to put the username and password. The email is optional. This will generate a file called `db.sqlite3` which is the database where all the blog content is stored.

After that, you have to make a migration, to create the tables in your database. To do that:

	$ python manage.py makemigrations
	$ python manage.py migrate

In another terminal you have to run django development server:

	$ python manage.py runserver  

In a browser put the link: [http://localhost:8000/admin/](http://localhost:8000/admin/)

The panel will ask you to add username and password. Once you are in Django dashboard you can start adding content to your blog.

To work with disqus comments you have to get your `DISQUS_API_KEY` and `DISQUS_WEBSITE_SHORTNAME`. They can be obtained at https://disqus.com/api/applications/.

NOTE: As of March 2017, [Disqus shows ads](https://kinsta.com/blog/disqus-ads/) by default. However, ads can be disabled if you run a [small and non-commercial site](https://blog.disqus.com/advertising-will-remain-optional-for-over-95-of-sites-on-disqus).

## Set up the project in a Ubuntu VPS server

First make sure that you have installed `git`, `apache2` and `libapache2-mod-wsgi` as explained before. Also, change the key in `private.py`.

	$ cd /var/www
	$ git clone https://github.com/miguelgfierro/sciblog.git
	$ cd sciblog
	$ cp sciblog/private.template.py sciblog/private.py
	$ python manage.py syncdb
	$ python manage.py makemigrations
	$ python manage.py migrate

Set the correct permissions:

	$ chown www-data:www-data /var/www/sciblog
	$ chown www-data:www-data /var/www/sciblog/db.sqlite3
	$ chown www-data:www-data /var/www/sciblog/img

Configure apache (in sciblog.conf change example.com for your url):

	$ cp sciblog.conf /etc/apache2/sites-available/
	$ a2ensite sciblog.conf
	$ a2enmod wsgi
	$ a2enmod rewrite
	$ a2enmod expires
	$ a2enmod headers
	$ a2enmod deflate
	$ a2enmod http2
	$ systemctl restart apache2

When you are in production you have to set `DEBUG_FLAG = False` in `sciblog/private.py`.

## Add your first content to the blog

The first step is to configure the site. Also, the first time you enter in your admin console [http://localhost:8000/admin/](http://localhost:8000/admin/), you have to go to sites and edit the default site, which is `example.com`. Change it for `localhost:8000`, if you are in development or to the name of your site without `http://` (my case would be miguelgfierro.com).

This will set the first entry in the database to your site, which is related to the variable `SITE_ID = 1` in `sciblog/settings.py`. You can see the number of the site in [http://localhost:8000/admin/sites/site/1/](http://localhost:8000/admin/sites/site/1/). If you add another site, then it will have a different number in the database, so for everything to work you have to change the variable `SITE_ID`. In my experience, it is better if you don't touch anything :-)

Press add in Post to add your first post. You can add different sections, images and formulas. For images the recommended width is `300px`. If you use a formula please select the flag `Post with Latex formula`. This will load the necessary js module to render the Latex code. If the flag is not activated, then the js is not added to the template (we don't want extra page load if we are not using formulas, right?).

You will see that your blog is working properly going to the url: [http://localhost:8000](http://localhost:8000) (in production you'll have to add something like http://miguelgfierro.com).

## Create flat pages: generic page, about page and privacy page

Go to the admin console and add your first flat page. A flat page is a static html code.

In Flat pages press add. In url put `/about/` (don't forget / in both sides). In title put your name, in sites put your site, in content put whatever you want and finally in template name put `flatpages/about.html`.

You can also create a privacy policy flat page. Go to the admin console, add a new flat page and in the url put `/privacy/`. I created a policy that is compliant with GDPR and that contains the typical systems and services of a normal personal blog: Google Analytics, cookies, RSS, etc. The text that I use can be found [here](blog/templates/privacy_template.md). You can adapt your policy to your specific blog.

In case you want to add more flat pages, there is a generic html template that you can customize by modifying the file [default.html](blog/templates/desktop/flatpages/default.html).

## Managing mobile view

In order to debug with a mobile phone first you need to set `DEBUG = True` in `sciblog/settings.py`. Then you have to run the django server in the computer's external IP. To do that:

	$ python manage.py runserver 0.0.0.0:8000

Then you need to know the IP of your computer. In Linux and Mac the command is `ifconfig`, in Windows is `ipconfig`. Then, to access your computer's server from a mobile phone, you have to open a browser in the phone and put the IP you just get. Let's assume the IP in my computer is 192.168.1.5, then you put in your mobile browser:

	http://192.168.1.5:8000 

## Secure page with SSL certificate (optional)

You can install a free SSL certificate with [Let's Encrypt](https://letsencrypt.org/). Google prioritizes pages with [SSL security](http://googlewebmastercentral.blogspot.be/2014/08/https-as-ranking-signal.html), so https has became a key element for SEO. The first step is to set to True the flag `HTTPS` in `settings.py`.

In order to activate the SSL, make sure you assign your domain to the IP of the VPS. For that, go to your DNS configuration and add an A entry with:
* Domain: example.com
* Type: A
* Target: <YOUR_IP>

Also add:
* Domain: www.example.com
* Type: CNAME
* Target: example.com

The basic installation in an apache server is very straightforward, as it is explained [here](https://letsencrypt.org/getting-started/). In the file sciblog.conf you have the configuration to activate the SSL. Furthermore, it allows to redirect http://example.com, https://example.com, http://www.example.com to https://example.com.

	$ snap install --classic certbot
	$ ln -s /snap/bin/certbot /usr/bin/certbot
	$ certbot --apache -m your_email@example.com -d example.com -d www.example.com
	$ a2enmod ssl
	$ systemctl restart apache2

When the certificate expires, you just need to renew it. 

	$ certbot renew --quiet --no-self-upgrade
	$ systemctl restart apache2
	
To check the installed certificates:

	$ certbot certificates

Once the SSL certificate is installed, you can check the security of your page using [this web](https://www.ssllabs.com/ssltest/index.html).

### Automatize renewal of Let's Encrypt certificate

This task can be automated as Let's Encrypt explains in their [web](https://letsencrypt.org/getting-started/) or you can use a CRON task. Edit crontab with `crontab -e` and add:

	7 7 */5 * * (/bin/date && certbot renew --quiet --keep-until-expiring --no-self-upgrade) >> cron.log 2>&1

This files executes every 5 days at 7.07am (you can see the explanation [here](https://crontab.guru/#7_7_*/5_*_*)). You can see that the CRON task is correctly set up typing `crontab -l`. Also, to make sure that the CRON job has run, you can type `grep "certbot" /var/log/syslog`.

## Speed up page with Cloudflare (optional)

You can use [Cloudflare](https://www.cloudflare.com/) to speed up your page and protect it. You just need to change the DNS. Don't forget to set the Cloudflare flag in `sciblog/private.py`.

NOTE: if you decide to set the SSL certificate along with Cloudflare, it is better to pause Cloudflare while installing the SSL certificate to check that it is working correctly in your server. Later, you can resume CloudFlare and go to Crypto and set SSL to full strict. This process is automated in the script [cron_ssl_renew.py](cron_ssl_renew.py). To activate this, edit crontab with `crontab -e` and add:

	7 7 */5 * * (/bin/date && /usr/bin/python /var/www/sciblog/cron_ssl_renew.py) >> cron.log 2>&1

## SEO tricks

This blog is automatically optimized for [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization), however, you can improve your visibility with these tricks:

* Always use https instead of http.
* Add your sitemap to [Google](https://www.google.com/webmasters/tools), [Bing](https://www.bing.com/webmaster/home/mysites) and [Yandex](https://webmaster.yandex.com/). For Baidu, it is difficult to index your site, in [this url](http://ping.baidu.com/ping.html) you can add your blog.
* Check the speed of your page with tools like [GTmetrix](https://gtmetrix.com), [Pingdom](https://tools.pingdom.com/), [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) or [Google page speed](http://developers.google.com/speed/pagespeed/insights/).
* Promote your posts in sites like [Hacker News](https://news.ycombinator.com/newest), [Reddit](http://reddit.com/), [Linkedin](http://linkedin.com/), [Facebook](http://facebook.com/) or [Twitter](http://twitter.com/).
* Analyze your site on [Google Analytics](https://analytics.google.com/analytics/web).
* Always use images in your posts, research shows that you will get [more views](https://www.b2bmarketing.net/en-gb/resources/news/research-news-articles-images-get-94-more-views-those-without).
* Engage with top influencers in your niche. You can feature other bloggers in your site and ask them to share or ask them to repost your content.
* Analyze your web with SEO checkers like [Woorank](https://www.woorank.com/) or [Semrush](https://www.semrush.com/).

This is how my web looks like in terms of speed using [GTmetrix](https://gtmetrix.com):

<p align="center">
	<img src="img/pagespeed.png" alt="Performance scores" width="90%"/>
</p>
