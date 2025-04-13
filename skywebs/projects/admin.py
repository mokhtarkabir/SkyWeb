# admin.py
from django.contrib import admin
from .models import Projects

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'preview_type', 'created_at')
    list_filter = ('category', 'preview_type')
