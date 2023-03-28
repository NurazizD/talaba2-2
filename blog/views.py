from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
from django.db.models import Q
# Create your views here.
def post_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        post = Post.objects.filter(Q(title__icontains=q))
    else:
        post = Post.objects.all()
    return render(request,'blog/list.html',{"post":post})

class detail_view(DetailView):
    model = Post
    template_name = 'blog/detail.html'