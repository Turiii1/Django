from django.db import models

# Create your models here.

class Category(models.Model):
    item_emer = models.CharField(max_length=50,null=True,blank=True)
    item_desct = models.TextField(max_length=500,null=True,blank=True)
    item_images = models.ImageField(upload_to="category/",null=True,blank=True)




class Item(models.Model):
    item_title = models.CharField(max_length=100,null=True,blank=True)
    item_desc = models.TextField(max_length=500,null=True,blank=True)
    item_image = models.ImageField(upload_to="item/",null=True,blank=True)
    item_category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)


class Review(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    surname = models.CharField(max_length=100,null=True,blank=True)
    position = models.CharField(max_length=100,null=True,blank=True)
    comment=models.TextField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to="item/",null=True,blank=True)

class Contact(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    surname=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    comment=models.TextField(max_length=500,null=True,blank=True)