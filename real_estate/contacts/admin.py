from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'message', 'phone', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    list_filter = ('listing', 'name')
    search_fields = ('name', 'listing', 'email', 'phone', 'message')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
