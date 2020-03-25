from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(max_length=500, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, null=True)
    email = models.EmailField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.name)