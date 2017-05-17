# blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tag_list','content_size', 'status',
                    'created_at', 'updated_at']
    actions = ['make_published', 'make_draft', 'make_Withdrawn']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')

    def tag_list(request, post):
        return ', '.join(tag.name for tag in post.tag_set.all()) # list comprehension 문법

    def content_size(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status ='p')
        self.message_user(request, '{} sucessfully marked as published'.format(updated_count))

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status ='d')
        self.message_user(request, '{} sucessfully marked as draft'.format(updated_count))

    def make_Withdrawn(self, request, queryset):
        updated_count = queryset.update(status ='w')
        self.message_user(request, '{} sucessfully marked as Withdrawn'.format(updated_count))

#admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'post_content_len']
    #list_select_related = ['post']

    def post_content_len(self, comment):
        return '{}글자'.format(len(comment.post.content))

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('post')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass