from django.db import models

class image(models.Model):
    name=models.IntegerField()
    image1=models.ImageField(upload_to='images/')