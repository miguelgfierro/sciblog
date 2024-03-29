import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site
from libs.ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    """Post class to generate blog posts."""

    title = models.CharField(max_length=67, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)
    # Description for SEO purposes
    meta_description = models.CharField("Meta description for SEO", max_length=155)
    abstract = models.TextField("Abstract (300-500 characters)", max_length=500)
    pub_date = models.DateField("Date published")
    keywords = models.CharField(max_length=100, blank=True)
    authors = models.CharField(max_length=100)
    youtube_video_id = models.CharField(
        "YouTube video ID (optional)",
        max_length=100,
        blank=True,
        help_text="Note: if the YouTube url is https://www.youtube.com/watch?v=fbu2cYW08HQ, the ID is fbu2cYW08HQ"
    )
    site = models.ForeignKey(Site)
    # If has_latex_formula=true, mathjax.js is included in template (better for SEO)
    has_latex_formula = models.BooleanField("Post with LATEX formula?", default=False)
    content = RichTextUploadingField(blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        """Returns the url for the current post.

        Returns:
            str: The url for the current post.
        """
        return "/blog/%s/%s/" % (self.pub_date.year, self.slug)

    def was_published_recently(self):
        """Checks if the post was published recently.

        Returns:
            bool: True if the post was published recently, False otherwise.
        """
        return self.pub_date >= timezone.now().date() - datetime.timedelta(days=7)

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"

    def save(self):
        self.slug = slugify(self.title)
        self.keywords = self.keywords.lower()
        super(Post, self).save()

    class Meta:
        ordering = ["-pub_date"]
