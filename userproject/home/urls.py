from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

urlpatterns = [
    path("",views.index,name='index'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutuser,name='logout'),
    path("signup",views.signupuser,name='signup')
]