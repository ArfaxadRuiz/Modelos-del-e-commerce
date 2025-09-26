from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # UserCreationForm guarda y hashea la contraseña
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
            messages.success(request, f"Usuario {username} creado correctamente.")
            return redirect("dashboard") # ruta "dashboard"
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})