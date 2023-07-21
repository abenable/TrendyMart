from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, ProfileImgForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import User, Profile


# Create your views here.

@login_required
def index(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'cart/index.html', {'profile': profile})
    except:
        pass
    return render(request, 'cart/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully')
            return redirect('/')
        return redirect('/login/')
    else:
        form = RegisterForm()
        return render(request, 'cart/register.html', {'form': form})


@login_required
def upload_profile_pic(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileImgForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            profile.update_image(image)
            messages.success(request, 'Profile picture uploaded successfully')
            return redirect('/')
    else:
        form = ProfileImgForm()
        return render(request, 'cart/upload.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request, email=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'cart/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
