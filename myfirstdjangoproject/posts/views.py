from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at');
    return render(request, 'posts/post_list.html', {'posts': posts})

from django.shortcuts import render, get_object_or_404

def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})