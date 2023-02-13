from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Profile, Post


# Create your views here.
def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'landing-page.html')


def login_view(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {'page': page}
    return render(request, 'core/login.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_form = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            Profile.objects.create(user=user_form, name=username)
            login(request, user)
            return redirect('home')

    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('landing-page')


@login_required(login_url='login')
def home(request):
    posts = Post.objects.all().order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'core/index.html', context)


@login_required(login_url='login')
def profile(request, pk):
    user_profile = Profile.objects.get(user=pk)
    posts = Post.objects.filter(author=user_profile.user)
    context = {'profile': user_profile, 'posts': posts}
    return render(request, 'core/profile.html', context)


@login_required(login_url='login')
def add_photo(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        caption = request.POST['caption']
        Post.objects.create(
            author=request.user,
            caption=caption,
            image=image
        )
        return redirect('home')

    return render(request, 'core/add-photo.html')


@login_required(login_url='login')
def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        caption = request.POST.get('caption')
        post.caption = caption
        post.save()
        return redirect('home')

    context = {'post': post}
    return render(request, 'core/edit-post.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    context = {'post': post}
    return render(request, 'core/delete-post.html', context)
