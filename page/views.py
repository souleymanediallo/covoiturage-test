from django.shortcuts import render
from covoiturage.models import Covoiturage


# Create your views here.
def home(request):
    covoiturages = Covoiturage.objects.all()[:4]
    context = {'covoiturages': covoiturages}
    return render(request, "page/index.html", context)