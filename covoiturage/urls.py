from django.urls import path
from . import views

urlpatterns = [
    path('', views.CovoiturageListView.as_view(), name="covoiturage-list"),
    path('<int:pk>', views.CovoiturageDetailView.as_view(), name="covoiturage-detail"),
    path('<int:pk>/update', views.CovoiturageUpdateView.as_view(), name="covoiturage-update"),
    path('<int:pk>/delete', views.CovoiturageDeleteView.as_view(), name="covoiturage-delete"),
    path('new', views.CovoiturageCreateView.as_view(), name="covoiturage-form"),
]