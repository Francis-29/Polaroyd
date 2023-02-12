from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name="landing-page"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),

    path('home/', views.home, name="home"),
    path('add-photo/', views.add_photo, name="add-photo"),
    path('profile/', views.profile, name="profile"),
]

htmx_urlpatterns = [
    path('check-username/', views.check_username, name='check-username')
]