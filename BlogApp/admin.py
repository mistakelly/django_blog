from django.contrib import admin
from BlogApp.models import Post


# Registered Models.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_display = [
        "title",
        "slug",
        "author",
        "created_at",
        "updated_at",
        "published_at",
    ]

    list_filter = ['created_at', 'published_at', 'author']
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ['author']
    date_hierarchy = 'published_at'
    ordering = ['created_at', 'published_at']
 
