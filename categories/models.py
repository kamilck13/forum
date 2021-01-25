from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title