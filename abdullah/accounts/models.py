from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

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
    image = models.ImageField(upload_to='projects/', default='default.jpg', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    



