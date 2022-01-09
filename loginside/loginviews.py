from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import tbl_Authentication

def base(request):
    return render(request, 'base.html')
     
 
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        try:
            user = tbl_Authentication.empAuth_objects.get(username=username,password=password)
            if user is not None:               
                return render(request, 'upload.html', {})
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
    
                return redirect('/')
        except Exception as identifier:
            
            return redirect('/')
    
    else:
        return render(request, 'upload.html')