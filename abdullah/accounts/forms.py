from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Project

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','email')
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=[
            'title',
            'description',
            'image',
            'tags',
            'demo_link',
            'github_link',
            'published'
        ]
        
        