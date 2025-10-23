from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/',blank=True,null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug=slugify(self.title)
            slug=base_slug
            num=1
            while Project.objects.filter(slug=slug).exists():
                slug=f"{base_slug} - {num}"
                num +=1
                self.slug=slug
                super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('project_detail',kwargs={'slug':self.slug})
    
                

    def __str__(self):
        return self.title

    
class ProjectImage(models.Model):
    project=models.ForeignKey('Project',on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='ProjectImage')
    caption=models.CharField(max_length=50,blank=True)
    
    
    def __str__(self):
        return f"{self.project.title} - {self.caption or 'Image'}"
    
    



