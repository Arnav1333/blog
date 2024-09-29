from django.shortcuts import render,redirect
from .forms import UserRegisterForm,PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Posts
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

# Create your views here.
def home(request):
    return render(request,'home.html')

def blog(request):
    return render (request,'blog.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('home') 

def post_list(request):
    posts = Posts.objects.all().order_by('-date_posted')
    return render(request,'post_list.html',{'posts':posts}) 

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-list')
        
    else:
        form = PostForm()
    return render(request,'post_form.html',{'form':form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to Update this post.")
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    
    
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    
    return render(request, 'post_confirm_delete.html', {'post': post})

