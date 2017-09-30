from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    create_time = models.DateTimeField()

    def __str__(self):
        return self.title


class biji(models.Model):
    href = models.CharField(max_length=64)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.href

class jsbooks(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()

    def __str__(self):
        return self.title