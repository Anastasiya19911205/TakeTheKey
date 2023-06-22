from django.db import models

# Create your models here.

class Users(models.Model):
    login = models.CharField(max_length=30, unique=True)
    password = models.IntegerField(unique=True)

    def __str__(self):
        return self.login

class Windows(models.Model):
    name_windows = models.CharField(max_length=30)
    code_windows = models.CharField(max_length=30)
    license_windows = models.IntegerField()
    user = models.ManyToManyField("Users")

    def __str__(self):
        return self.name_windows

class Ivi (models.Model):
    name_ivi = models.CharField(max_length=30)
    code_ivi = models.CharField(max_length=30)
    license_ivi = models.IntegerField()
    user = models.ManyToManyField("Users")

    def __str__(self):
        return self.name_ivi