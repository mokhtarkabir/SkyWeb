from django.contrib import admin
from .models import Blog, Category, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'published_at', 'views')
    list_filter = ('is_published', 'category', 'author')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)
    date_hierarchy = 'published_at'
    list_editable = ('is_published',)
    readonly_fields = ('views', 'created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category', )
        }),
        ('Content', {
            'fields': ('content', 'image'),
            'classes': ('collapse',),
        }),
        ('Publication', {
            'fields': ('is_published', 'published_at'),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)