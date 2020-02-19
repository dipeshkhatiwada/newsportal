from django.db import models
from django.core.exceptions import ValidationError
from django import forms


# Create your models here.

class Advertisement(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='adds/')
    view_count = models.IntegerField(default=0,null=True, blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "advertisement"