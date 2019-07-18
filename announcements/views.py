from django.shortcuts import render, get_object_or_404
from .models import Announcement
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import io 
from django.http import FileResponse
from reportlab.pdfgen import canvas 


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
    announcement = get_object_or_404(Announcement, pk=announcement_id)
    context = {
        'announcement' : announcement
    }
    return render(request, 'announcements/announcement.html', context)

def search(request):
    return render(request, 'announcements/search.html')


# Generate PDF 
def create_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100,100, "Hello Admin")

    p.showPage()
    p.save()

    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

