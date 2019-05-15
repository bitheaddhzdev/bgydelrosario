from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='announcements'),
    path('<int:announcement_id>', views.announcement, name='announcement'),
    path('search', views.search, name='search'),
]