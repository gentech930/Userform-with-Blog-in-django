from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        # Username aur password POST request se hasil karain
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # User ko authenticate karain
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Agar user valid hai to usay login karain
            auth_login(request, user)
            return redirect('index')  # Login ke baad user ko index page par redirect karain
        else:
            # Agar authentication fail ho jaye, to error message ke sath login page dubara render karain
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    # Agar GET request aaye to login page render karain
    return render(request, 'login.html')

@login_required
# def index(request):
#     return render(request, 'index.html')  # Login ke baad index.html page render karega

def user_logout(request):
    auth_logout(request)
    return redirect('login')  # Logout ke baad login page par redirect karain


