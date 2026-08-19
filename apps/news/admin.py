from django.contrib import admin

# Register your models here.

from apps.news.models import News, NewsCategory

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ('title',)
