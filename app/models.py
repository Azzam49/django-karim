from django.db import models

# Create your models here.
class Students(models.Model):
    # https://docs.google.com/spreadsheets/d/1HbxbGMj871pJwRKxQ-kIwWLWhZHm0flN8v9e0GeCYEc/edit?usp=sharing
    name = models.CharField(max_length=50) # required
    age = models.IntegerField(blank=True, null=True) # optional