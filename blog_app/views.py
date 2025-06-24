from django.shortcuts import render, HttpResponse
from . models import Post

# Create your views here.

def home(request):
    #return HttpResponse('This is home page')

    objects = Post.objects.all()
    return render(request, 'html/base.html', context = {'objects': objects})

def view_post(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'html/view_post.html', context = {'post': post})