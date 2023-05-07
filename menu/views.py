from django.shortcuts import render

# Create your views here.

def menu_index(request):
    return render(request, 'menu/pizza_menu.html')

def drink_index(request):
    return render(request, 'menu/drink_menu.html')

def sides_index(request):
    return render(request, 'menu/side_menu.html')
