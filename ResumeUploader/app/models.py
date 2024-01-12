from django.db import models

# Create your models here.

class Resume(models.Model):
    
    
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Locality=models.CharField(max_length=100)
    City=models.CharField(max_length=50)
    Pin=models.PositiveIntegerField()
    State=models.CharField(max_length=50)
    Mobile_No=models.PositiveIntegerField()
    Email=models.EmailField()
    Job_City=models.CharField(max_length=50)
    Profile_Image=models.ImageField(null=False,blank=False)
    
    