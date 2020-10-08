from django.db import models
from django.contrib.auth.models import User
from .choices import profile_choices, place_choices, bagage_choices, car_choices
from django.urls import reverse


# Create your models here.
class Covoiturage(models.Model):
    profile = models.CharField(max_length=200, verbose_name="Vous êtes ?", choices=profile_choices)

    start_destination = models.CharField(max_length=200, verbose_name="Adresse de départ")
    end_destination = models.CharField(max_length=200, verbose_name="Adresse d'arrivée")

    date_depart = models.DateField(verbose_name="Date de départ")
    time_depart = models.TimeField(verbose_name="Heure de départ")

    siege = models.CharField(verbose_name="Nombre de place disponible", max_length=200, choices=place_choices)
    price = models.PositiveIntegerField(verbose_name="Prix par passager")

    voiture = models.CharField(max_length=200, choices=car_choices, blank=True, null=True, verbose_name="Type de voiture")

    bagage = models.CharField(max_length=200, choices=bagage_choices, verbose_name="Type de Bagage")

    smoking = models.BooleanField(default=False, verbose_name="Êtes-vous un fumeur ?")
    information = models.TextField(blank=True, null=True, verbose_name="Information sur votre trajet")

    certificated = models.BooleanField(default=False)
    activated = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('covoiturage-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.profile

