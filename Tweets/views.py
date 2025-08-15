from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TweetForm
from .models import Tweet

@login_required
def post_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, 'Your tweet has been posted!')
            return redirect('Tweets:post_tweet')
        else:
            pass
    else:
        form = TweetForm()

    tweets = Tweet.objects.all()

    return render(request, 'Tweets/post_tweet.html', {'form': form, 'tweets': tweets})

def home(request):
    tweets = Tweet.objects.all()
    return render(request, 'Tweets/home.html', {'tweets': tweets})