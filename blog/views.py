# blog/views.py

from django.shortcuts import render
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