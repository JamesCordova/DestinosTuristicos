from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

# Create your models here.
class Destination(models.Model):
    nombre = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')# necesario pip install Pillow
    descripcion = models.TextField()
    precio = models.IntegerField()
    oferta = models.BooleanField(default = False)

    def get_absolute_url(self):
        return reverse('', kwargs={'myID': self.id})