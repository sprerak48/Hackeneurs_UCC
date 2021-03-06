from django.db import models
from django.contrib.auth.models import User
import hashlib

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description1 = models.IntegerField(default=0, blank=True, null=True)
    description2 = models.IntegerField(default=0, blank=True, null=True)
    description3 = models.IntegerField(default=0, blank=True, null=True)
    cryptoname = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(
        default='media/mainpage4.jpg', blank=True, null=True)
    confirmhash = models.CharField(max_length=100, blank=True, null=True)
    
    

    def __str__(self):
        return  self.user.username

    # def createhash(self, email):
    #     hash = hashlib.sha1()
    #     temp = email + 'hahaha'
    #     hash.update(temp.encode('utf-8'))
    #     tp = hash.hexdigest()
    #     print(tp)
    #     self.confirmhash = tp
