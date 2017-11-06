from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Feedback(models.Model):
    email = models.EmailField(null=False)
    content = RichTextUploadingField(config_name='default')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email+' '+str(self.created)

    def get_absolute_url(self):
        return reverse('acm:feedback_detail', kwargs={'pk': self.pk})


class UpcomingEvents(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(config_name='default')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

