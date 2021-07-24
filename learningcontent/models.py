from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



