from django.db import models


class product(models.Model):
    name = models.CharField(max_length=255)
    mood_intensity = models.IntegerField()
    description = models.TextField()

