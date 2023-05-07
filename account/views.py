from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'account/account.html')

def login_index(request):
    return render(request, 'account/login_screen.html')

def create_index(request):
    return render(request, 'account/create_account.html')