from django.db import models
import datetime
from django.utils import timezone
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.db.models.signals import post_save


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True,editable=False)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return "/blog/category/%s/" % (self.slug)

    def save(self):
        self.slug = slugify(self.title)
        super(Category,self).save()

    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True,editable=False)
    body = models.TextField()
    pub_date = models.DateField('Date published')
    category = models.ForeignKey(Category, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    site = models.ForeignKey(Site, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.pub_date.year, self.slug)

    def was_published_recently(self):
        return self.pub_date >= timezone.now().date() - datetime.timedelta(days=7)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def save(self):
        self.slug = slugify(self.title)
        super(Post,self).save()

    class Meta:
        ordering = ["-pub_date"]

