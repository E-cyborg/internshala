from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .forms import UserCreateForm,LoginForm
from django.contrib.auth.decorators import login_required
from aUTH.models import cuser


@login_required
def user_view(request):
    return render(request, 'user.html', {'user': request.user})
        


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = form.cleaned_data["email_or_username"]
            password = form.cleaned_data["password"]

            user = cuser.objects.filter(email=email_or_username).first()
            if user:
                user = authenticate(request, username=user.username, password=password)
            else:
                user = authenticate(request, username=email_or_username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def LogoutView(req):
    if req.method=='GET':
        logout(req)
    return redirect('/login')

def RegisterView(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreateForm()
    return render(request, 'register.html', {'form': form})

