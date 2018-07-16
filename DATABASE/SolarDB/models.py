from django.db import models
from datetime import datetime 


# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length = 255,   default = "")
    details = models.CharField(max_length = 255,   default = "")
    date = models.CharField(max_length = 255,   default = "")
    
    
class User(models.Model):
    username = models.CharField(max_length = 255,   default = "")
    password = models.CharField(max_length=50)
    choices = ((0, 'Regular User'), (1, 'Admin'))
    accountType = models.IntegerField(choices=choices, default = 0)
    
    
    