from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def title(request):
    return render(request, 'title.html')

def sign(request):
    if request.user.is_authenticated:
        return redirect('lobby')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.saveUser()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('lobby')
        else: 
            context = {"mainmessage":'Error', 'form': form}
            return render(request, "msg.html", context) 
    return redirect('sign')

def signin(request):
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lobby')
        else:
            context = {"mainmessage":'Invalid'}
            return render(request, "msg.html", context)
    return redirect('sign')

def signout(request):
    logout(request)
    context = {"mainmessage":'Logged out'}
    return render(request, "msg.html", context)

def lobby(request):
    if request.user.is_authenticated:
        return render(request, 'lobby.html')
    return redirect('sign')

def room(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            room_name = request.POST["room_name"]
            return render(request, 'room.html', {
                'room_name': room_name
            })
        return redirect('lobby')
    return redirect('sign')
