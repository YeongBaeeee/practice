# accounts/urls.py

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from .forms import LoginForm


urlpatterns =[
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login/$', auth_view.login, name='login',
        kwargs={
            'authentication_form' : LoginForm,
            'template_name' : 'accounts/login_form.html'
        }),
    url(r'^logout/$', auth_view.logout, name='logout',
        kwargs={
            'next_page' : settings.LOGIN_URL
        }),
    url(r'^profile/$', views.profile, name='profile'),
]