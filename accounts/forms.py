# accounts/form.py

from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
       # fields = ('username', 'email')
        fields = UserCreationForm.Meta.fields + ('email',)
