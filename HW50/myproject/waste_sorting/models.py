import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=140)
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        if self.author:
            return f"{self.author.email:.20} : {self.id} : {self.comment:.100}{'...' if len(self.comment) > 100 else ''}"

        else:
            return f"<Deleted>: {self.comment} : {self.id} : {self.comment:.100}{'...' if len(self.comment) > 100 else ''}"


class Profile(models.Model):
    avatar = models.TextField(max_length=10)
    age = models.IntegerField()
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)


class NameField(models.CharField):

    def get_prep_value(self, value):
        return str(value).lower()


class WasteContainer(models.Model):
    cont_type = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='static/img', height_field=None, width_field=None, max_length=100)

    class Meta:
        ordering = ('cont_type',)

    def __str__(self):
        return self.cont_type


class Waste(models.Model):
    waste_name = NameField(max_length=150)
    type = models.ManyToManyField(WasteContainer)

    class Meta:
        ordering = ('waste_name',)

    def __str__(self):
        return self.waste_name

    def get_url(self):
        return reverse('waste_details', args=[self.id])

# Create your models here.
