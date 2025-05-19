# main/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to='project_images/', blank=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    features = models.TextField(blank=True, help_text="Use bullet points or comma-separated features.")
    results = models.TextField(blank=True, help_text="Describe the impact or results of the project.")

    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']