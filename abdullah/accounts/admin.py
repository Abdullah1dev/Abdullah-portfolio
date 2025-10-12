from django.contrib import admin
from .models import CustomUser, Project, Tag


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)  
    ordering = ('-created',)   


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'published', 'updated_at')
    list_filter = ('published', 'tags')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}  
    ordering = ('-updated_at',)

     



