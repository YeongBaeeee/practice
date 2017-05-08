# blog/models.py
import re
from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms import ValidationError
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type!')

class Post(models.Model):
    STATUS_CHOICES =(
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_post_set')
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력해 주세요. 최대 100자 내외.')
                          #   choices=(
                          #       ('제목1', '제목1레이블'),
                          #       ('제목2', '제목2레이블'),
                          #       ('제목3', '제목3레이블'),
                          #   ))
    content = models.TextField(verbose_name='내용')
    photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d',
                                       processors=[Thumbnail(300, 300)],
                                       format='JPEG',
                                       options={'quality' : 60}
                                       )
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='위도/경도 포맷으로 입력하세요.',
                              blank=True, validators=[lnglat_validator])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id'] #필드에 대해서 내림차순 정렬 [id]는 오름차순 정렬

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True) #같은 테그테이블에 테그이름이 겹치지 않게..

    def __str__(self):
        return self.name