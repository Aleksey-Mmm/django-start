"""
URL configuration for al1_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
from hello import views

product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
]

urlpatterns = [
    path("user_get/", views.user_get),
    re_path(r"products/(?P<id>\d+)/", include(product_patterns)),
    path("", views.index),
    re_path(r"^user3/(?P<name>\D+)/(?P<age>\d+)", views.user3),
    re_path(r"^user3/(?P<name>\D+)", views.user3),
    re_path(r"^user3", views.user3),
    path("user/<str:name>", views.user),
    path("user2", views.user2),
    path("user2/<name>", views.user2),
    path("user2/<name>/<int:age>", views.user2),
    path("index", views.index),
    path("zag3", views.zag_3),
    path("zag2", views.zag_2),
    re_path(r"^zag", views.zag),
    re_path(r"^about", views.about, kwargs={"name":"Alex", "age": 50}),
    re_path(r"^contact", views.contact),
]
