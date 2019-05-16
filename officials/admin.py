from django.contrib import admin

from .models import Official

class OfficialAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'middle_name', 'last_name', 'email', 'phone', 'position')
    list_display_links = ('id', 'first_name', 'middle_name', 'last_name')
    search_fields = ('first_name', 'middle_name', 'last_name')
    
admin.site.register(Official,OfficialAdmin)
