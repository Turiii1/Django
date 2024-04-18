from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    reviews=Review.objects.all()
    shows=Category.objects.all()
    items=Item.objects.all()
    context={"items":items,"shows":shows,"reviews":reviews }
    return  render(request,'home.html',context)   

def about(request):
    shows=Category.objects.all()
    context={"shows":shows }
    return  render(request,'about.html',context)   

def contact(request):
    shows=Category.objects.all()
    if request.method== "POST":
        email_info = request.POST["email"]
        comment_info = request.POST["comment"]
        name_info=request.POST["name"]
        surname_info=request.POST["surname"]

        Contact(email=email_info,comment=comment_info,name=name_info,surname=surname_info).save()
    context={"shows":shows }
    return  render(request,'contact.html',context)   

def details(request,id):
    shows=Category.objects.all()
    item=Item.objects.get(pk=id)
    context={"item":item,"shows":shows}
    return render(request,'detailitem.html',context)

def services(request,id):
    elementCategory=Item.objects.filter(item_category=Item)
    show=Category.objects.get(pk=id)
    context={"show":show,"elementCategory":elementCategory}
    return render(request,'custom.html',context)


