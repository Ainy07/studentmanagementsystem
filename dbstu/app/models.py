from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.IntegerField()
    password = models.CharField(max_length=200)
    
    
class Course(models.Model):
    name = models.CharField(max_length=200)
    fees = models.IntegerField()
    duration = models.CharField(max_length=300)
    comments = models.TextField()   