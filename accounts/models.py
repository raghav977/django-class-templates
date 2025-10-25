from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=100,default="address")


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    authorname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    ads = models.ImageField(upload_to='ads/', null=True, blank=True)