from django.db import models

# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='static/images')
    Name=models.CharField(max_length=30,null=True)
    description=models.CharField(max_length=150)
    
    