from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField

class Profile(models.Model):
    
    name = models.CharField(max_length = 200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)  
    password = models.CharField(max_length=32,null=True)
    image = models.ImageField(null= True,blank=True)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




