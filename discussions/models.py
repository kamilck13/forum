from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel

from categories.models import Category


class Discussion(TimeStampedModel):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('discussion-detail', kwargs={'pk': self.pk})
