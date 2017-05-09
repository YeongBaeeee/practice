#blog/views_cbv.py

from django.views.generic import CreateView
from .models import Post
from django import forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# 원래는 별로도 blog/forms.py에 구현해야하지만, 안헷갈리게 하기위해.. 나중에 수정할듯?!

post_list = ListView.as_view(model=Post, paginate_by=5)

post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

post_new = CreateView.as_view(model=Post, fields= '__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url='/blog/')
