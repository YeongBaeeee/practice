# blog/views.py

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

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
