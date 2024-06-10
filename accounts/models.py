from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


#https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class User(AbstractUser):
    photos_uploaded = models.PositiveIntegerField(verbose_name='photos_uploaded', default=0)
    likes_earned = models.PositiveIntegerField(verbose_name='likes_earned', default=0)
