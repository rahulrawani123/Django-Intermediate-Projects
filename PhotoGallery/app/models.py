from django.db import models

# Create your models here.

class Category(models.Model):
    Name=models.CharField(max_length=100,null=False,blank=False)
    
    def __str__(self):
        return self.Name
    

class Photos(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(null=False,blank=False)
    Description=models.TextField(null=False,blank=False)
     
    def __str__(self):
        return self.Description
