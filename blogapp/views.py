from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.datetime.now()
    new_blog.body = request.POST['content']
    new_blog.save()
    return redirect('home')

def delete(request, delete_blog_id):
    delete_blog = get_object_or_404(Blog,pk = delete_blog_id)
    delete_blog.delete()
    return redirect('home')

def edit(request, edit_blog_id):
    edit_blog = get_object_or_404(Blog, pk=edit_blog_id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request, update_blog_id):
    update_blog = get_object_or_404(Blog, pk=update_blog_id)
    update_blog.title= request.POST["title"]
    update_blog.writer = request.POST['writer']
    update_blog.body=request.POST['content']
    update_blog.save()
    return redirect('home')

def search(request):
    q=request.GET['q']
    ans = Blog.objects.filter(title=q)
    return render(request, 'search.html', {'q':q, 'ans':ans})
    