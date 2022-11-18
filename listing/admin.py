from django.contrib import admin
from .models import *


class ListingAdmin(admin.ModelAdmin):

    list_display =  ('id', 'title', 'is_published', 'price')
    list_display_links = ('id', 'title')
    list_filter = ('bedrooms', 'price', 'state')
    list_editable = ('is_published',)
    search_fields = ('title', 'desc', 'address', 'city', 'state', 'zipcode', 'price', 'bedrooms')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)