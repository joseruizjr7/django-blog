from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import Post
from django.http import HttpResponse
from blog.forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'

def post_datail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create a Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the commetn to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    return render(request, template_name, {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })
