from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'announcement', 'email', 'contact_date')
    list_display_links = ('id', 'name', 'announcement')
    search_fields = ('name', 'announcement', 'email')
    lst_per_page = 25
admin.site.register(Contact, ContactAdmin)