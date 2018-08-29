from django.db import models

# Create your models here.
class Snippet(models.Model):
    name = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    phone = models.CharField(max_length=140)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=140)
    comment = models.TextField(max_length=1400)
    
    def __str__(self):
        return self.name