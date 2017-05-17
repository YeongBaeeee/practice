# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Post, Comment
from .forms import PostForm
from django.contrib import messages

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '') #q가 있으면 가져오고 없으면 빈문자열가져옴
    if q:
        qs = qs.filter(title__contains=q)

    return render(request, 'blog/post_list.html',
                  {
                      'post_list': qs,
                      'q' : q,
                  })

def post_detail(requset, id):
    '''
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    '''

    post = get_object_or_404(Post, id=id)

    return render(requset, 'blog/post_detail.html',{
        'post': post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post) # post.get_absolute_url()이 구현되어있음 url을 통해서 이동
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html',
                  {
                      'form' : form,
                  })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정했습니다.')
            return redirect(post) # post.get_absolute_url()이 구현되어있음 url을 통해서 이동
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html',
                  {
                      'form' : form,
                  })

def comment_list(request):
    comment_list = Comment.objects.all().select_related('post')
    return render(request, 'blog/comment_list.html', {
        'comment_list' : comment_list,
    })