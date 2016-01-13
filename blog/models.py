import datetime
from time import time

from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site
import markdown2
from django.db.models.signals import post_delete
from django.dispatch import receiver
from libs.ckeditor_uploader.fields import RichTextUploadingField
from libs.ckeditor.fields import RichTextField
from libs.markdown2Mathjax.lib.markdown2Mathjax import sanitizeInput, reconstructMath


def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    year = datetime.datetime.now().year
    return str(year) + '/' + str(int(time())) + '.' + ext

class Post(models.Model):
    title = models.CharField(max_length=67, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True,editable=False)
    meta_description = models.CharField('Meta description for SEO', max_length=155)
    abstract = models.TextField('Abstract (300-500 characters)',max_length=500)
    pub_date = models.DateField('Date published')
    keywords = models.CharField(max_length=100, blank=True)
    authors = models.CharField(max_length=100, blank=True, null=True)
    site = models.ForeignKey(Site, blank=True, null=True)
    image = models.ImageField(upload_to=generate_filename, blank=True, null=True)
    image_caption = models.CharField(max_length=200, blank=True)
    image_second = models.ImageField(upload_to=generate_filename, blank=True, null=True)
    image_caption_second = models.CharField(max_length=200, blank=True)
    youtube_link = models.URLField(blank=True)
    has_latex_formula = models.BooleanField(default=False)

    content = RichTextUploadingField(blank=True, null=True)
    #content = RichTextField(blank=True, null=True)

    #Paper of maximum 2 pages (1 mandatory + 1 optional)
    body_page1_col1 = models.TextField('Body 1,1 (1000-1200 characters)')
    body_page1_col1_html = models.TextField(editable=False, blank=True, null=True)
    body_page1_col2 = models.TextField('Body 1,2 (600-700 characters)')
    body_page1_col2_html = models.TextField(editable=False, blank=True, null=True)
    body_page2_col1 = models.TextField('Body 2,1 (2100-2200 characters)', blank=True)
    body_page2_col1_html = models.TextField(editable=False, blank=True, null=True)
    body_page2_col2 = models.TextField('Body 2,2 (2100-2200 characters)', blank=True)
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

        temp11 = sanitizeInput(self.body_page1_col1)
        markdown11 = markdown2.markdown(temp11[0], extras=['fenced-code-blocks'])
        self.body_page1_col1_html = reconstructMath(markdown11, temp11[1])
        temp12 = sanitizeInput(self.body_page1_col2)
        markdown12 = markdown2.markdown(temp12[0], extras=['fenced-code-blocks'])
        self.body_page1_col2_html = reconstructMath(markdown12, temp12[1])
        temp21 = sanitizeInput(self.body_page2_col1)
        markdown21 = markdown2.markdown(temp21[0], extras=['fenced-code-blocks'])
        self.body_page2_col1_html = reconstructMath(markdown21, temp21[1])
        temp22 = sanitizeInput(self.body_page2_col2)
        markdown22 = markdown2.markdown(temp22[0], extras=['fenced-code-blocks'])
        self.body_page2_col2_html = reconstructMath(markdown22, temp22[1])

        super(Post,self).save()

    class Meta:
        ordering = ["-pub_date"]

@receiver(post_delete, sender=Post)
def stuff_post_delete_handler(sender, **kwargs):
        Post = kwargs['instance']
        storage, path = Post.image.storage, Post.image.path
        storage.delete(path)

