from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User ,auth
from django.contrib import messages

# Create your views here.

# def index(request):
#     Feature1 = Feature()
#     Feature1.id = 0
#     Feature1.is_true = True
#     Feature1.name = 'Fast'
#     Feature1.details  = 'our service is very good and quick as well as excelence'
    
#     Feature2 = Feature()
#     Feature2.id = 1
#     Feature2.is_true = True
#     Feature2.name = 'Reliable'
#     Feature2.details  = 'our service is very good and quick as well as reliable'

#     Feature3 = Feature()
#     Feature3.id = 2
#     Feature3.is_true = False
#     Feature3.name = 'Easy To Use'
#     Feature3.details  = 'our service is very good and quick as well as easy to use'

#     Feature4 = Feature()
#     Feature4.id = 3
#     Feature4.is_true = True
#     Feature4.name = 'Affordable'
#     Feature4.details  = 'our service is very good and quick as well as affordable'    
    
#     Features = [Feature1,Feature2,Feature3,Feature4]
def index(request):
    Features = Feature.objects.all()
    return render(request,'index.html',{'Features':Features})

def register(request):
    if request.method == 'POST':
        
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']
       
       if password == password2:
           if User.objects.filter(email=email).exists():
               messages.info(request, 'Email Already In Used')
               return render(request,'register.html')
            #    return redirect('register')
           elif User.objects.filter(username=username).exists():
               messages.info(request, 'Username Already In Used')
               return render(request,'register.html')
           else:
               user = User.objects.create_user(username=username, email=email, password=password)
               user.save()
               return redirect('login')
        # else:
        #     messages.info(request,'register')  
    else:        
        return render(request,'register.html')