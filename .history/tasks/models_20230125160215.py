from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.models.CharField(max_length=50)
