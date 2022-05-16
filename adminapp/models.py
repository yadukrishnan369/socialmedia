from django.db import models

# Create your models here.


class AdminSignup(models.Model):
    userName=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    