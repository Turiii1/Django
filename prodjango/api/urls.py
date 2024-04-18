from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="homePage"),
    path('about/',views.about, name="aboutPage"),
    path('contact/',views.contact, name="ctaboutPage"),
    path('preview/<id>',views.details, name="details"),
    path('show/<id>',views.services,name="showpage"),
]

