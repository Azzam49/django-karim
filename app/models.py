from django.db import models

# Create your models here.
class Students(models.Model):
    # https://docs.google.com/spreadsheets/d/1HbxbGMj871pJwRKxQ-kIwWLWhZHm0flN8v9e0GeCYEc/edit?usp=sharing
    name = models.CharField(max_length=50) # required
    age = models.IntegerField(blank=True, null=True) # optional

    # Note :
        # - Any new column you create, better to make it as optional.

    def __str__(self):
        return f"{self.name} | Age : {self.age}"

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    subject = models.CharField(max_length=20)

    def __str__(self):
        return f"Name {self.name} | Age: {self.age}, | Subject: {self.subject}"
