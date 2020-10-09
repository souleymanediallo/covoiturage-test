from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('profile/update', views.profileupdate, name="profile-update"),
    path('register', views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
]