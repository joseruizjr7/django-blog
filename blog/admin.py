from django.contrib import admin
from blog.models import Post
from django.contrib.auth.models import User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'excerpt',
        'author',
        'status',
        'created_at',
    )