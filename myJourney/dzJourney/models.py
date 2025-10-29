# ...existing code...
from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    # photo removed to avoid requiring Pillow

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"


class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='journey_images/', blank=True, null=True, help_text='Upload an image for this milestone')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Learning Milestone"
        verbose_name_plural = "Learning Milestones"
        ordering = ['-date']
# ...existing code...