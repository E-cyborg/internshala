from django.shortcuts import render, redirect
from .form import login_form,UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from .task import send__email

def LoginView(req):
    if req.user.is_authenticated:
        return redirect('home')
    if req.method == 'POST':
        form = login_form(req.POST)
        if form.is_valid():
            username = form.cleaned_data['email_or_username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                send__email.delay(req.user.email)  
                return redirect('home')
            else:
                return render(req, 'login.html', {
                    'form': form,
                    'error_message': 'Invalid credentials'
                })
        else:
            return render(req, 'login.html', {'form': form})
    else:
        form = login_form()
        return render(req, 'login.html', {'form': form})


def UserRegisterView(req):
    if req.user.is_authenticated:
        return redirect('home')
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in after registration
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(req, user)
            return redirect('home')
        else:
            return render(req, 'sign.html', {
                'form': form,
                'error_message': 'Invalid form submission.'
            })
    else:
        form = UserCreationForm()
        return render(req, 'sign.html', {'form': form})

def LogoutView(req):
    if req.method =='GET':
        logout(req)
    return redirect('home')


def home(req):
    return HttpResponse('<h1>heelo</h1>')