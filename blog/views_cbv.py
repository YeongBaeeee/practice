#blog/views_cbv.py

from django.views.generic import CreateView
from .models import Post
from django import forms
from django.views.generic import ListView, CreateView, DetailView


# 원래는 별로도 blog/forms.py에 구현해야하지만, 안헷갈리게 하기위해.. 나중에 수정할듯?!

post_list = ListView.as_view(model=Post, paginate_by=3)

post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class  = PostForm
    #success_url = 'blog:post_detail' # 원래해야하는데 나중으로 미뤄두기

post_new = PostCreateView.as_view()