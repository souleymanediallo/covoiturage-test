from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Covoiturage
from django.urls import reverse_lazy

# Create your views here.
class CovoiturageListView(ListView):
    model = Covoiturage
    template_name = "covoiturage/covoiturage_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['covoiturages'] = Covoiturage.objects.all().order_by('-date_depart')
        return context


class CovoiturageDetailView(DetailView):
    model = Covoiturage
    template_name = "covoiturage/covoiturage_detail.html"
    context_object_name = "covoiturage"


class CovoiturageCreateView(CreateView):
    model = Covoiturage
    fields = ['profile', 'start_destination', 'end_destination', 'date_depart', 'time_depart', 'siege', 'price', 'voiture', 'bagage', 'smoking', 'information' ]
    context_object_name = "forms"
    template_name = "covoiturage/covoiturage_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CovoiturageUpdateView(UpdateView):
    model = Covoiturage
    fields = ['profile', 'start_destination', 'end_destination', 'date_depart', 'time_depart', 'siege', 'price', 'voiture', 'bagage', 'smoking', 'information' ]
    context_object_name = "forms"
    template_name = "covoiturage/covoiturage_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CovoiturageDeleteView(DeleteView):
    model = Covoiturage
    success_url = reverse_lazy('covoiturage-list')
