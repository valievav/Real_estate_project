from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'city', 'state', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('city', 'state', 'realtor')
    list_editable = ('is_published', 'price')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zip_code', 'price')
    list_per_page = 20


admin.site.register(Listing, ListingAdmin)
