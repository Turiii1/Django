from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Contact)