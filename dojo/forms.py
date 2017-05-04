# dojo/forms.py
from django import forms
from django.core.validators import MinLengthValidator
from .models import Post, GameUser

SERVER_CHOICES = (
    ('A', 'A서버'),
    ('B', 'B서버'),
    ('C', 'C서버'),
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent' : forms.HiddenInput
        }
    '''
    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
            return post
    '''
class GameUserSignupForm(forms.ModelForm):
    '''
    server_name = forms.ChoiceField(choices=SERVER_CHOICES)
    username = forms.CharField(max_length=20,
                               validators=[MinLengthValidator(3)],
                               error_messages={'min_length':'3글자 이상입력하세요.'})
    '''
    class Meta:
        models = GameUser
        #fields = ['title', 'content']
        #fields = '__all__'
        fields = ['server_name', 'username']

    def clean_username(self):
        return self.cleaned_data.get('username', '').strip()

    def __str__(self):
        return self.server_name

class GameUserSignupForm2(forms.Form):
    server_name = forms.ChoiceField(choices=SERVER_CHOICES)
    username = forms.CharField(max_length=20,
                               validators=[MinLengthValidator(3)],
                                error_messages={'min_length':'3글자 이상입력하세요.'})

    def clean_username(self):
        return self.cleaned_data.get('username', '').strip()

    def __str__(self):
        return self.server_name
