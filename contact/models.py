from django.db import models
from django.core.exceptions import ValidationError
from django import forms


# Create your models here.

class Contact(models.Model):
    name = models.CharField(
        verbose_name="नाम (अनिवार्य)",
        max_length=200
        )
    email = models.EmailField(
        verbose_name="इमेल (अनिवार्य)",
        unique=True
    )
    subject = models.CharField(
        verbose_name="विषय (अनिवार्य)",
        max_length=200
    )
    message = models.TextField(
        verbose_name="प्रतिक्रिया दिनुहोस्",
        null=True, blank=True
    )
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "contact"