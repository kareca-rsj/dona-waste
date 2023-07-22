"""
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import User
from django.contrib import messages

def register_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if (User.objects.filter(username=username)):
            messages.info(request, "Username already taken!")
        elif (User.objects.filter(email=email)):
            messages.info(request, "Email already taken!")
        elif (password == confirm_password):
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect("authentication:login")
        else:
            messages.info(request, "Your confirmed password is different!")
    return render(request, "register.html")

def login_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #TODO: Redirect to landing page here!
        messages.info(request, "Wrong username or password!")
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("authentication:login")
    """