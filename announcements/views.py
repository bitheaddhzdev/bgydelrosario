from django.shortcuts import render

def index(request):
    return render(request, 'announcements/announcements.html')

def announcement(request):
    return render(request, 'announcements/announcement.html')

def search(request):
    return render(request, 'announcements/search.html')


