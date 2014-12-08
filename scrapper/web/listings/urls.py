from django.conf.urls import include, url
from django.contrib import admin
from listings import views

urlpatterns = [
    url(r'^search/', views.search),
    url('/', views.search)
]