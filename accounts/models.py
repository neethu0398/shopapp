from django.db import models

# Create your models here.

class register(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=150)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=150)
    def __str__(self):
        return self.firstname
