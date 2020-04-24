from django.contrib import admin
from .models import Category, News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ['created','title']
    list_display = ['title','created','updated','slug','image']
    list_display_links = ['title','image']
    search_fields = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}




admin.site.register(Category)
admin.site.register(Comment)

