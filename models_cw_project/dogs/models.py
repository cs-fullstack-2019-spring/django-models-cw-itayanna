

#importing models function

from django.db import models

# Create your models here.


# problem1 model

class Dogs(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)

# problem2 model

class Account(models.Model):
    username = models.CharField(max_length=200)
    realName = models.CharField(max_length=200)
    accountNumber = models.IntegerField()
    accountBalance = models.DecimalField(decimal_places=2, max_digits=200)
