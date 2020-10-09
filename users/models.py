from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos", default="photos/souleymane.png", blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    presentation = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

