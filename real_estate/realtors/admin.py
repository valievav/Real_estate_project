from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp', 'hire_date', 'is_published')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp', 'is_published')
    search_fields = ('name', )
    list_per_page = 20


admin.site.register(Realtor, RealtorAdmin)
