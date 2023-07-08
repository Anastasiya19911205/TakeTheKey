from django.db import models

# Create your models here.

class Users(models.Model):
    login = models.CharField(max_length=30, unique=True)
    password = models.IntegerField(unique=True)

    def __str__(self):
        return self.login

class Windows(models.Model):
    name_windows = models.CharField(max_length=30)
    code_windows = models.CharField(max_length=30,unique=True)
    license_windows = models.CharField(max_length=30,unique=True)
    user = models.ManyToManyField("Users")

    def __str__(self):
        return self.name_windows

class Ivi (models.Model):
    name_ivi = models.CharField(max_length=30)
    code_ivi = models.CharField(max_length=30,unique=True)
    license_ivi = models.CharField(max_length=30,unique=True)
    user = models.ManyToManyField("Users")

    def __str__(self):
        return self.name_ivi

class Antivirus (models.Model):
    name_antivirus = models.CharField(max_length=30)
    code_antivirus = models.CharField(max_length=30, unique=True)
    license_antivirus = models.CharField(max_length=30, unique=True)
    user = models.ManyToManyField("Users")

    def __str__(self):
        return self.name_antivirus