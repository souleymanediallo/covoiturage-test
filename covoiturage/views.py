from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Covoiturage
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class CovoiturageListView(ListView):
    model = Covoiturage
    template_name = "covoiturage/covoiturage_list.html"
    ordering = ['-date_depart']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['covoiturages'] = Covoiturage.objects.all().order_by('-date_depart')
        return context


class CovoiturageDetailView(LoginRequiredMixin, DetailView):
    model = Covoiturage
    template_name = "covoiturage/covoiturage_detail.html"
    context_object_name = "covoiturage"


class CovoiturageCreateView(LoginRequiredMixin, CreateView):
    model = Covoiturage
    fields = ['profile', 'start_destination', 'end_destination', 'date_depart', 'time_depart', 'siege', 'price', 'voiture', 'bagage', 'smoking', 'information' ]
    context_object_name = "forms"
    template_name = "covoiturage/covoiturage_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CovoiturageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Covoiturage
    fields = ['profile', 'start_destination', 'end_destination', 'date_depart',
              'time_depart', 'siege', 'price', 'voiture', 'bagage', 'smoking', 'information']
    context_object_name = "forms"
    template_name = "covoiturage/covoiturage_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        covoiturage = self.get_object()
        if self.request.user == covoiturage.author:
            return True
        return False


class CovoiturageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Covoiturage
    success_url = reverse_lazy('covoiturage-list')

    def test_func(self):
        covoiturage = self.get_object()
        if self.request.user == covoiturage.author:
            return True
        return False
