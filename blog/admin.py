from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_by', 'published_at',)
    list_filter = ('category',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('title',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
