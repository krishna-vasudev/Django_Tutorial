from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from myapp import views

urlpatterns = [
    path("",views.index,name='home'),
    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about'),
    path("summary",views.summary,name='summary')
]