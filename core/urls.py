from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name="landing-page"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),

    path('home/', views.home, name="home"),
    path('add-photo/', views.add_photo, name="add-photo"),
    path('edit-post/<int:pk>/', views.edit_post, name="edit-post"),
    path('delete-post/<int:pk>/', views.delete_post, name="delete-post"),
    path('profile/<int:pk>/', views.profile, name="profile"),
    path('profile-edit/', views.profile_edit, name="profile-edit"),

    path('like/<int:pk>/', views.like, name="like"),

]

