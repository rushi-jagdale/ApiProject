from django.db import models

# Create your models here.
class Advisor(models.Model):
    name = models.CharField( max_length=50)
    imageUrl = models.URLField()