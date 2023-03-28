from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=700)
    body = models.TextField()
    data = models.DateTimeField(auto_now_add=True)