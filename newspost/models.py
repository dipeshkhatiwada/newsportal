from django.db import models
from django.core.exceptions import ValidationError
from django import forms


# Create your models here.
def customLengthValidator(value):
    if len(value) > 5:
        return True
    else:
        raise ValidationError("must have more than 5 chars")


def atValidator(value):
    if '@' in value:
        raise ValidationError("title cannot have @  chars")
    else:
        return True
STATUS_BUTTON= [
    ('1', 'Active'),
    ('0', 'Deactive'),
   ]

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, validators=[customLengthValidator, atValidator, ])
    slug = models.SlugField(max_length=100, unique=True,  validators=[customLengthValidator, atValidator, ])
    status = models.BooleanField(default=True)
    menu_display = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True,  validators=[customLengthValidator, atValidator, ])
    description = models.TextField(null=True, blank=True)
    view_count = models.IntegerField(default=0,null=True, blank=True)
    #  null is related to database and  blank is related to form
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    # auto now provide today date
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # django will atomically add _id in foreign key

    def __str__(self):
        return self.title

    # class Meta:
        
        # fields = ['__all__']
        # widgets = {'view_count': forms.HiddenInput()}
        # it will name the database table
# from django.db import models

# # Create your models here.
