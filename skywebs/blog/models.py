from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
# category of blogs Eg: Sport, Technology, and etc...
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# blog model section 
class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# commetn section ob blog 
# where people who see the blog they can add comment and reply to comments

class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"

    class Meta:
        ordering = ['created_at']
