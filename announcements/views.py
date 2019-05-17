from django.shortcuts import render
from .models import Announcement

def index(request):
    announcements = Announcement.objects.all()

    context = {
        'announcements' : announcements,    
    }
    return render(request, 'announcements/announcements.html', context)

def announcement(request):
    return render(request, 'announcements/announcement.html')

def search(request):
    return render(request, 'announcements/search.html')


