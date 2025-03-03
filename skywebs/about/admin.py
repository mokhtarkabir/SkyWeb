from django.contrib import admin
from .models import AboutPage, TeamMember
from django.utils.safestring import mark_safe

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display the title in the admin list view
    search_fields = ('title', 'description')  # Enable search by title and description

# 
# team member admin section
# 

class TeamMemberAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('display_image','fullName', 'skill', )
    
    # Enable search functionality for these fields
    search_fields = ('fullName', 'skill')
    
    # Add filters for these fields
    list_filter = ('skill',)
    
    # Make the fields editable directly from the list view
    
    # Set the number of items displayed per page in the admin list view
    list_per_page = 20

     # Custom method to display the image in the admin list view
    def display_image(self, obj):
        if obj.image:
            return mark_safe( f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />')
        return "No Image"
    
    display_image.short_description = 'Image'  # Column header name

# Register the model with the custom admin class
admin.site.register(TeamMember, TeamMemberAdmin)