from django.db import models

# Create your models here.
#we create/define database here
class Note(models.Model):
    body=models.TextField(null=True,blank=True)#agar user form mai null values bhi daale then also we accept it
    updated=models.DateTimeField(auto_now=True)#this will update time everytime we save files
    created=models.DateTimeField(auto_now_add=True)#this will not always update when we make instruction to it then only it updates


def __str__(self):
    return self.body[0:50]#first 50 char
