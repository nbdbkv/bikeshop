from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm
from .models import Category, Bike

# Create your views here.
def home(request, category_slug=None):
    category_page = None
    bikes = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        bikes = Bike.objects.filter(category=category_page)
    else:
        bikes = Bike.objects.all()
    return render(request, 'home.html', {'category': category_page, 'bikes': bikes})

def about(request):
    return render(request, 'about.html')

def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('home')

def detail(request):
    return render(request, 'detail.html')
