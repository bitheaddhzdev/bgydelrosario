from django.shortcuts import render
from .models import Announcement
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
def index(request):
    announcements = Announcement.objects.order_by('-date').filter(is_published=True)
    paginator = Paginator(announcements, 6)
    page = request.GET.get('page')
    page_announcements = paginator.get_page(page)
    context = {
        'announcements' : page_announcements,    
    }
    return render(request, 'announcements/announcements.html', context)

def announcement(request, announcement_id):
    return render(request, 'announcements/announcement.html')

def search(request):
    return render(request, 'announcements/search.html')


