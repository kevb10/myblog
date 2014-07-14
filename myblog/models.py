from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('new')

    def recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    recently_published.admin_order_field = 'pub_date'
    recently_published.boolean = True
    recently_published.short_description = 'Published recently?'

'''
class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment_text = models.TextField(max_length=500)
    pub_date = models.DateTimeField('date comment published')

    def __unicode__(self):  # Python 3: def __str__(self):
        	short = self.comment_text[:30]
        	return short
'''