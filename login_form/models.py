from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=5, )