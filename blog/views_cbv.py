#blog/views_cbv.py

from django.views.generic import CreateView
from .models import Post
from django import forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# 원래는 별로도 blog/forms.py에 구현해야하지만, 안헷갈리게 하기위해.. 나중에 수정할듯?!


class PostListView(ListView):
    model = Post
    queryset = Post.objects.prefetch_related('tag_set', 'comment_set').all()
    paginate_by = 5

post_list = PostListView.as_view()

#post_list = ListView.as_view(model=Post,
#                             queryset=Post.objects.prefetch_related('tag_set', 'comment_set').all(),
#                             paginate_by=5)

post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

post_new = CreateView.as_view(model=Post, fields= '__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
