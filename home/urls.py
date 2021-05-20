from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from home import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path("blogpost", views.blogpost, name="blogpost"),
    path("blogpost/blog/<int:id>", views.blog, name="blog"),
    path('writeablog', views.writeablog, name="writeablog"),
    path('admin/', views.admin, name="admin"),
    path('accounts/admin/', views.accadmin, name="accadmin"),
    path('accounts/login', include('django.contrib.auth.urls')),
    path('accounts/signup', include('django.contrib.auth.urls')),
    path('accounts/logout', include('django.contrib.auth.urls')),
    path('pagenotfound/', views.error_404, name="error404"),
] 
