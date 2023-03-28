from django.db import models
from django.urls import reverse
# Create your models here.
class Pupil(models.Model):
    ism =  models.CharField(max_length=250)
    yosh = models.IntegerField(null=True,blank=True)
    tugulgan_kun = models.CharField(max_length=250,null=True,blank=True)
    guruh = models.CharField(max_length=250)
    tel_raqam = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('home')
    def __str__(self):
        return self.ism

class versiya(models.Model):
    link = models.CharField(max_length=10000000)
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name