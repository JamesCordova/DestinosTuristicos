from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Destination(models.Model):
    nombre = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    descripcion = models.TextField()
    nombre = models.CharField(default = False)