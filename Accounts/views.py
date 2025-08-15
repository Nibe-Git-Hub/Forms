from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('Tweets:post_tweet')
        else:
            pass
    else:
        form = UserRegistrationForm()
    return render(request, 'Accounts/register.html', {'form': form})