from django.contrib import admin
from blog.models import Post, Comment, Category, Tag
from django.contrib.auth.models import User

admin.site.site_header = 'Blog Administration'
admin.site.site_title = 'Blog'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'category', 'author', 'status', 'created_at', )
    list_filter = ('status', 'created_at', 'updated_at', )
    list_editable = ('status', )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)