from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def logOut(request):
    if request.user is not None:
        logout(request)

    return redirect('/')
