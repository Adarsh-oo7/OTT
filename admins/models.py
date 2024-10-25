from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class customUser(AbstractUser):
    email=models.CharField(max_length=30,unique=True)
    username = models.CharField(max_length=150, unique=False) 
    token=models.CharField(max_length=40,null=True)
    block=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 