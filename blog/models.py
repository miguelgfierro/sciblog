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
import markdown2
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver

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

def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    year = datetime.datetime.now().year
    return str(year) + '/' + str(int(time())) + '.' + ext

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True,editable=False)
    abstract = models.TextField(blank=True)
    pub_date = models.DateField('Date published')
    category = models.ForeignKey(Category, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    site = models.ForeignKey(Site, blank=True, null=True)
    image = models.ImageField(upload_to=generate_filename, blank=True, null=True)
    image_caption = models.CharField(max_length=200, blank=True)

    #Paper of maximum 2 pages (1 mandatory + 1 optional)
    body_page1_col1 = models.TextField()
    body_page1_col1_html = models.TextField(editable=False, blank=True, null=True)
    body_page1_col2 = models.TextField()
    body_page1_col2_html = models.TextField(editable=False, blank=True, null=True)
    body_page2_col1 = models.TextField(blank=True)
    body_page2_col1_html = models.TextField(editable=False, blank=True, null=True)
    body_page2_col2 = models.TextField(blank=True)
    body_page2_col2_html = models.TextField(editable=False, blank=True, null=True)

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
        self.body_page1_col1_html = markdown2.markdown(self.body_page1_col1, extras=['fenced-code-blocks'])
        self.body_page1_col2_html = markdown2.markdown(self.body_page1_col2, extras=['fenced-code-blocks'])
        self.body_page2_col1_html = markdown2.markdown(self.body_page2_col1, extras=['fenced-code-blocks'])
        self.body_page2_col2_html = markdown2.markdown(self.body_page2_col2, extras=['fenced-code-blocks'])
        super(Post,self).save()

    class Meta:
        ordering = ["-pub_date"]

@receiver(post_delete, sender=Post)
def stuff_post_delete_handler(sender, **kwargs):
        Post = kwargs['instance']
        storage, path = Post.image.storage, Post.image.path
        storage.delete(path)

