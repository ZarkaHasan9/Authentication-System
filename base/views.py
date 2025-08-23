from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return 'sucess'
        else:
             form = UserCreationForm()
        return render(request,'auth/register.html',{'form': form})

        

    return render(request, 'signup.html')

@login_required
def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')
