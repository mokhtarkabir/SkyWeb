from django.contrib import admin

# Register your models here.
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_name')  # Display these fields in the admin list view
    search_fields = ('title', 'description')  # Enable search by title and description