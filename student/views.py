from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register_trainer(request):
      if request.method=='POST':
            username = request.POST['user_name']
            password = request.POST['pass_word'] 
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('login_trainer')
      else:
            return render(request,'register.html')
      
def login_trainer(request):
      if request.method=='POST':
            username = request.POST['user_name']
            password = request.POST['pass_word']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                  login(request,user)
                  return redirect('trainer_home')
            else:
                  msg = 'username and password not matching'
                  return render(request,'login.html',{'msg':msg})
                  
      else:
            return render(request,'login.html')
      
@login_required(login_url='login_trainer')
def trainer_home(request):
      return render(request,'trainer_home.html')

def logout_trainer(request):
      logout(request)
      return redirect('login_trainer')

@login_required(login_url='login_trainer')
def update_profile(request):
      if request.method=='POST':
             id=request.POST['id']
             name=request.POST['name']
             address=request.POST['address']
             department=request.POST['department']
             age=request.POST['age']
             gender=request.POST['gender']
             phone=request.POST['phone']
             email=request.POST['email']
             married=request.POST['married']
             joining_date=request.POST['joining date']
             print(
                   id,name,address,department,
                   age,gender,phone,email,married,joining_date
             )            
             return redirect('trainer_home') 
      else:
            return render(request,'edit_profile.html')