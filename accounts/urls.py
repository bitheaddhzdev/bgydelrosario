from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),

]