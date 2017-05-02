# dojo/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title', 'content']

    '''
    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
            return post
    '''