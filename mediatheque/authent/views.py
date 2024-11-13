from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from authent.forms import LoginForm
from users.models import User

def login_user(request):
    form = LoginForm()
    user = User.objects.all()
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                message = "Le nom d'utilisateur ou/et le mot de passe sont invalides."
            else:
                login(request, user)
                if user.is_staff:
                    return redirect("home")
                else:
                    return redirect("users_home")
    return render(
        request, "authent/login.html", {"form": form, "message": message}
    )


def logout_user(request):
    logout(request)
    return redirect("login") 
