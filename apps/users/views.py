from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect

from apps.users.models import Users

# Create your views here.
class Login(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
