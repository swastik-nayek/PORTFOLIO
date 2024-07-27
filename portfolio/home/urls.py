from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path("index",views.home, name='index'),
    path("contact",views.contact, name='contact'),
    path("about",views.about, name='about'),
    path("blogWrite",views.blogWrite, name='blogWrite'),
    path("blogHome",views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
    path("search",views.search, name='search'),
    # path("CV",views.CV, name='CV')
]
