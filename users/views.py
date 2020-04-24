from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Account created for {username}')
            return redirect('login')
        else:
            messages.warning(request,'The two password fields didn\'t match')
    else:
        form  = UserRegisterForm()

    context={
        'form':form,
    }

    return render(request,'users/register.html',context=context)



def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Username or Password is incorrect')
    return render(request,'users/login.html')


def auth_logout(request):
    logout(request)
    return render(request,'users/logout.html')

