from django.contrib import admin
from .models import *
# Register your models here.
class Pupil_admin(admin.ModelAdmin):
    list_display = ['ism','yosh','tugulgan_kun','guruh','tel_raqam']
admin.site.register(Pupil,Pupil_admin)
admin.site.register(versiya)