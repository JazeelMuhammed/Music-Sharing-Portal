from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'You have registered successfully')
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form':form})
