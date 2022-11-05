from django.contrib import admin
from .models import *


class MainStartPageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'description', 'text', 'image')
    search_fields = ('title', 'description', 'text')


class CategoryArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text',
                    'pub_date', 'image', 'category')
    search_fields = ('title', 'description', 'text')


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(CategoryArticles, CategoryArticlesAdmin)
admin.site.register(MainStartPage, MainStartPageAdmin)
