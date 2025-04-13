from django.db import models
from django.utils.text import slugify

class CarouselSlide(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Impressive title for the slide (e.g., 'Websites That Soar Above the Rest')"
    )
    bio = models.TextField(
        max_length=300,
        help_text="Short compelling bio/description for the slide"
    )
    image = models.ImageField(
        upload_to='carousel/',
        help_text="Upload an eye-catching image for this slide"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Should this slide be displayed?"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which slides appear (lower numbers first)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Carousel Slide"
        verbose_name_plural = "Carousel Slides"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Add any pre-save logic here if needed
        super().save(*args, **kwargs)