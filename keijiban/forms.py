from django import forms
from .models import User, Comment

class RegisterForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'email', 'age']

class PostForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['user', 'text']

        widgets = {
            'text': forms.Textarea
        }