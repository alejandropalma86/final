from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('author',)
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', )
    prepopulated_fields = {'slug': ('title',)}

    
admin.site.register(Post, PostAdmin)