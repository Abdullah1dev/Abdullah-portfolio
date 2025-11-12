from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Project
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

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
        
        
    
    
    def clean_image(self):
        image=self.cleaned_data.get('image')
        if image:
            if image.size > 2 * 1024 * 1024:
                raise ValidationError("Image size cannot exceeds 2MB..")
            return image
            
    
    def clean_demo_link(self):
        demo_link=self.cleaned_data.get('demo_link')
        if demo_link:
            validator=URLValidator()
            try:
                validator(demo_link)
            except ValidationError:
                raise ValidationError("Please Enter a Valid demo URL(must start with htttp or https)")
            
            return demo_link
        
    def clean_github_link(self):
        github_link=self.cleaned_data.get('github_link')
        if github_link:
            validator=URLValidator()
            try:
                validator(github_link)
            except ValidationError:
                raise ValidationError("Please Enter a valid git_hub link")
            return github_link
