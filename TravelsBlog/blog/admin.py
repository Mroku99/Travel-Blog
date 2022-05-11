from django.contrib import admin

from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'published']
    list_filter = ['author', 'created', 'updated']
    search_fields = ['title']
    raw_id_fields = ['author']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'created']
    list_filter = ['created', 'updated']
    search_fields = ['post', 'body']
