from django.db import models

class Algorithm(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.