from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully.")
            return redirect("signin")
    return render(request, "users_app/signup.html")

def signin_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # ✅ redirect to home instead of admin
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "users_app/signin.html")

@login_required
def home_view(request):
    return render(request, "users_app/home.html")


def signout_view(request):
    logout(request)
    return redirect('signin')
@login_required
def home_view(request):
    return render(request, 'users_app/home.html')  # create this template
