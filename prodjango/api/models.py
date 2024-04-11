from django.db import models

# Create your models here.

class Category(models.Model):
    item_emer = models.CharField(max_length=50,null=True,blank=True)
    item_images = models.ImageField(upload_to="category/",null=True,blank=True)




class Item(models.Model):
    item_title = models.CharField(max_length=100,null=True,blank=True)
    item_desc = models.TextField(max_length=500,null=True,blank=True)
    item_image = models.ImageField(upload_to="item/",null=True,blank=True)