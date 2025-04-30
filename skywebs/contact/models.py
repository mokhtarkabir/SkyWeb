from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone

class ContactSubmission(models.Model):
    # Contact information (matches your form fields)
    name = models.CharField(max_length=100, verbose_name="Your Name")
    email = models.EmailField(validators=[EmailValidator()], verbose_name="Your Email")
    project = models.CharField(max_length=200, blank=True, null=True, verbose_name="Project")
    message = models.TextField(verbose_name="Message")
    
    # Meta information
    submitted_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    
    # Status tracking
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='new'
    )
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"Contact from {self.name} - {self.project or 'No project'} ({self.status})"