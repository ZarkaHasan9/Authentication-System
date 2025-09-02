from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            messages.success(request, "Account created successfully! Please login.")
            # login(request,user)
            return redirect('login')
        else:
            messages.error(request, "Error creating account. Please try again.")
    else:
        # initial_data ={'username':'', 'password1':'', 'password2':''}
        form = UserCreationForm()
    return render(request,'auth/login.html',{"form_type": "register", "register_form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request,'auth/login.html',  {"form_type": "login", "login_form": form})


def logout_view(request):
    logout(request)
    return redirect('login')
