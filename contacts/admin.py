from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'listing', 'email', 'contacted_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
