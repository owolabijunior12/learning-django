from django.shortcuts import render
from .models import User
from django.http import HttpResponse

# Create your views here.
def register(request):
    return HttpResponse('Register Page');
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
        
    #     # Simple validation (you can expand this)
    #     if username and email and password:
    #         user = User(username=username, email=email, password=password)
    #         user.save()
    #         return render(request, 'register/success.html', {'user': user})
    #     else:
    #         error = "All fields are required."
    #         return render(request, 'register/register.html', {'error': error})
    
    # return render(request, 'register/register.html')
