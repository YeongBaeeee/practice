# blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status',
                    'created_at', 'updated_at']
    actions = ['make_published', 'make_draft', 'make_Withdrawn']

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
    pass