from django.contrib import admin

from .models import Service, Order

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'updated')

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = [ 'date' ]
    list_display = ('name', 'total',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
