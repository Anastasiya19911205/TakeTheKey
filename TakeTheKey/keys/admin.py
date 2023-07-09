from django.contrib import admin
from .models import *

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    fields = ['login', 'password']
    list_display = ["login", "password"]
    ordering = ['login']
    search_fields = ['login']

@admin.register(Windows)
class WindowsAdmin(admin.ModelAdmin):
    fields = ['name_windows', 'code_windows', 'license_windows']
    list_display = ["name_windows", "code_windows", 'license_windows']


@admin.register(Ivi)
class IviAdmin(admin.ModelAdmin):
    fields = ['name_ivi', 'code_ivi', 'license_ivi']
    list_display = ["name_ivi", "code_ivi", 'license_ivi']

@admin.register(Antivirus)
class AntivirusAdmin(admin.ModelAdmin):
    fields = ['name_antivirus', 'code_antivirus', 'license_antivirus']
    list_display = ["name_antivirus", "code_antivirus", 'license_antivirus']

# admin.site.register(Users)
# admin.site.register(Windows)
# admin.site.register(Ivi)
# admin.site.register(Antivirus)

# Register your models here.
