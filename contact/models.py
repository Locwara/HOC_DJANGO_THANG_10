from django.db import models

# Create your models here.
class contactForm(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()