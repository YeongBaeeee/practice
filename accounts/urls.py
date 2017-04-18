# accounts/urls.py

from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^profile/$', views.profile)
]