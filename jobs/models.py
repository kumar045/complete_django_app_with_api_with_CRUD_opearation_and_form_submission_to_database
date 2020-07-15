from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    types = models.CharField(max_length=100)
    signature = models.CharField(max_length=100)

    def __str__(self):
        return self.title
