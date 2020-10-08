from django.contrib import admin
from .models import Covoiturage


# Register your models here.
@admin.register(Covoiturage)
class CovoiturageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'siege', 'price')
    list_display_links = ('id', 'profile')