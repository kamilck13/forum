from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel

from discussions.models import Discussion


class Post(TimeStampedModel):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('discussion-detail', kwargs={'pk': self.discussion.pk})
        #return reverse('post-detail', kwargs={'pk': self.pk})