from django.db import models

# Create your models here.

class Service(models.Model):
    # Field for the icon (e.g., FontAwesome icon class name)
    icon_name = models.CharField(max_length=50, help_text="Enter the icon class name (e.g., 'fa fa-code')")

    # Field for the service title
    title = models.CharField(max_length=100, help_text="Enter the service title")

    # Field for the service description
    description = models.TextField(help_text="Enter a brief description of the service")

   

    class Meta:
        verbose_name = "Service"  # Singular name for the model
        verbose_name_plural = "Services"  # Plural name for the model

    def __str__(self):
        return self.title  # Display the title in the admin panel