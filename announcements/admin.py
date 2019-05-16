from django.contrib import admin

from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'date', 'official')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'location', 'official')
    list_per_page = 50
admin.site.register(Announcement, AnnouncementAdmin)