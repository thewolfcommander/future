from django.shortcuts import render, redirect
from django.contrib.auth.views import auth_login
from django.contrib.auth.decorators import login_required

from accounts.forms import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request, user)
            return redirect('accounts:profile')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
            

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {})
