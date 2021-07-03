from django.db import models

# Create your models here.
class Advisor(models.Model):
    name = models.CharField( max_length=50)
    imageUrl = models.URLField()


class Book(models.Model):
   
    adviser_id = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
