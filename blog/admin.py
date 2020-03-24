from django.contrib import admin
from blog.models import Post
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'excerpt',
        'author',
        'status',
        'created_at',
    )
    
    list_filter = (
        'status',
        'created_at',
        'updated_at',
    )

    list_editable = (
        'status',
    )

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)