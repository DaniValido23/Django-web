from django.contrib import admin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('author', 'published')
    list_display = ('title', 'get_name', 'published', 'post_categories')
    date_hierarchy = ('published')
    search_fields = ('title', 'author__first_name')
    list_filter = ('categories__name', 'author__first_name')

    def post_categories(self, post_obj):
        res = ''

        for c in post_obj.categories.all().order_by('name'):
            res += c.name + ', '

        res = res[:len(res) - 2]

        return res

    post_categories.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
