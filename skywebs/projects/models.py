# models.py
from django.db import models
from django.utils import timezone
class Projects(models.Model):
    PREVIEW_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('iframe', 'iFrame'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    preview_type = models.CharField(max_length=10, choices=PREVIEW_TYPE_CHOICES, default='image')
    preview_file = models.FileField(upload_to='project_previews/', blank=True, null=True,
                                    help_text="Upload image or video if not using iframe.")
    preview_url = models.URLField(blank=True, null=True,
                                  help_text="Use only if preview_type is 'iframe'.")
    download_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
