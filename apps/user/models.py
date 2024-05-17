from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    web_site = models.CharField(max_length=255, blank=True, verbose_name='Web site')
    twitter = models.CharField(max_length=255, blank=True, verbose_name='Twitter')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
