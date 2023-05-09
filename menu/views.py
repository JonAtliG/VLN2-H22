from django.shortcuts import render

# Create your views here.

def menu_index(request):
    return render(request, 'menu/pizza_menu.html')

def drink_index(request):
    return render(request, 'menu/drink_menu.html')

def sides_index(request):
    return render(request, 'menu/side_menu.html')

def create_pizza(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
        #TODO: instance new pizzacreateform()
    return render(request, 'pizza/create_pizza.html', {
        'form': form
})