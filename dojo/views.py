# dojo/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .forms import PostForm
from .models import Post
import os


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # 방법 1
            '''
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            '''
            # 방법 2
            '''
            post = Post.(title=form.Cleaned_data['title'],
                            content=form.cleaned_data['content'])
            post.save()
            '''
            # 방법 3
            '''
            post = Post.objects.create(title=form.cleaned_data['title'],
                                       content=form.cleaned_data['content'])
            '''
            # 방법 4 사전이니까 **로 언팩
            '''
            post = Post.objects.create(**form.cleaned_data)
            '''
            # 방법 5
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/') # 혹은 namespace:name 써도됨
    else:
        form = PostForm()

    return render(request, 'dojo/post_form.html',
                  {
                      'form' : form,
                  })

def mysum(request, numbers):
    return HttpResponse(sum(map(lambda s: int(s or 0), numbers.split('/'))))
     # int (s or 0) numbers가 거짓이면 0으로 바꿔줌

    #def mysum(request, x, y):
#    return HttpResponse(int(x) + int(y))


def hello(request, name, age):
    return HttpResponse('안녕하세요. {} {}살이시네요.'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>안녕하세요. 여러분의 파이썬/장고 페이스메이커가 되겠습니다.</p>
        '''.format(name=name))


def post_list2(request):
    name ='공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message' : '안녕, 파이썬&장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
        },json_dumps_params={'ensure_ascii':False},
        content_type=u"application/json; charset=utf-8",)

def excel_download(request):
    #filepath = '/home/ubuntu/askdjango/gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb')as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
