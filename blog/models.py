from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')
    text = models.TextField()

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)