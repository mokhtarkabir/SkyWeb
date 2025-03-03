from django.db import models

# Create your models here.

class AboutPage(models.Model):
    # Title of the about page
    title = models.CharField(max_length=200, help_text="Title of the about page")

    # Image for the about page
    image = models.ImageField(upload_to='about_images/', help_text="Image for the about page")

    # Description of the about page
    description = models.TextField(help_text="Description of the about page")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"


# team meber model

class TeamMember(models.Model):
    fullName = models.CharField(max_length=100, verbose_name="Full Name")
    skill = models.CharField(max_length=100, verbose_name="Skill")
    facebook_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Facebook URL")
    instagram_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Instagram URL")
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="LinkedIn URL")
    image = models.ImageField(upload_to='team_members/', blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return self.fullName

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"