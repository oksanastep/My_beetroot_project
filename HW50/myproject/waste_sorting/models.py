import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
import datetime


class NameField(models.CharField):

    def get_prep_value(self, value):
        return str(value).lower()


class Container(models.Model):
    type = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='static/img', height_field=None, width_field=None, max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('type',)

    def __str__(self):
        return self.type


class Waste(models.Model):
    name = NameField(max_length=150)
    container = models.ManyToManyField(Container)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('waste_details', args=[self.id])

# Create your models here.
