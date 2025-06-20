from time import sleep
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpRequest
from .forms import StudentRegistrationForm,StudentLoginForm
from django.contrib.auth import authenticate, login


def register_view(request : HttpRequest):
    print(request.POST)
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Account created! Please login.")
            sleep(3)
            return redirect('login')
    else:
        form = StudentRegistrationForm()
        
    return render(request,'user/register.html',{'form': form})

def login_view(request : HttpRequest):
    print(request.POST)
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data.get("password")
            user = authenticate(request,email=email,password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return render(request,"user/hello.html",{"name":user.name})
            else:
                messages.error(request, "Invalid email or password.")
            
    else:
        form = StudentLoginForm() 
    return render(request, "user/login.html", {"form": form})