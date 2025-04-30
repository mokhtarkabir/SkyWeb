from django.contrib import admin
from .models import ContactSubmission
# Register your models here.

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name','email','project',)
    search_fields = ('name',)