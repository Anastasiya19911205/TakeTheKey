from django.db import models

# Create your models here.

class Users(models.Model):
    login = models.CharField(max_length=30, unique=True)
    password = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural ='Users'

    def __str__(self):
        return self.login

class Windows(models.Model):
    name_windows = models.CharField(max_length=30)
    code_windows = models.CharField(max_length=30, unique=True)
    license_windows = models.CharField(max_length=30, unique=True)
    user = models.ManyToManyField("Users")

    class Meta:
        verbose_name_plural ='Windows'

    def __str__(self):
        return self.name_windows

class Ivi(models.Model):
    name_ivi = models.CharField(max_length=30)
    code_ivi = models.CharField(max_length=30, unique=True)
    license_ivi = models.CharField(max_length=30, unique=True)
    user = models.ManyToManyField("Users")

    class Meta:
        verbose_name_plural ='Ivi'

    def __str__(self):
        return self.name_ivi

class Antivirus (models.Model):
    name_antivirus = models.CharField(max_length=30)
    code_antivirus = models.CharField(max_length=30, unique=True)
    license_antivirus = models.CharField(max_length=30, unique=True)
    user = models.ManyToManyField("Users")

    class Meta:
        verbose_name_plural = 'Antivirus'

    def __str__(self):
        return self.name_antivirus


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()