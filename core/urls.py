from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name="landing-page"),
    path('home/', views.index, name="index"),
    path('profile/', views.profile, name="profile"),
]
