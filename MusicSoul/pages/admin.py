from django.contrib import admin

from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ['title']
    list_display = ('title', 'updated')
    search_fields = ('title', 'content')

admin.site.register(Page, PageAdmin)
