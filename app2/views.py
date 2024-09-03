from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def user_login(request):
    if request.method == 'POST':
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:

            auth_login(request, user)
            return redirect('index') 
        else:
            
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    
    return render(request, 'login.html')

@login_required
# def index(request):
#     return render(request, 'index.html')  # 

def user_logout(request):
    auth_logout(request)
    return redirect('login')  


