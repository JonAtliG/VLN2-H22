from django.shortcuts import render

# Create your views here.
pizzas = [
    {
        'name': 'Seweroni Pizza',
        'img': "/static/img/SeweroniPizza.png",
        'desc': 'Pepperoni, Cheese, Pizza Sauce',
        'price': 17.99,
    },
    {
        'name': "Seweroni Pizza",
        'img': "/static/img/SeweroniPizza.png",
        'desc': "Pepperoni, Cheese, Pizza Sauce",
        'price': 17.99
    },
    {
        'name': "Hawaian Sewer",
        'img': "/static/img/Hawaian%20Sewer.png",
        'desc': "Ham, Pineapple, Bacon, Cheese, Pizza Sauce",
        'price': 17.99
    },
    {
        'name': "Spicy Sewage",
        'img': "/static/img/SpicySewage.png",
        'desc': "Jalapeno, Paprika, Mushrooms, Onion, Cheese, Pizza Sauce",
        'price': 18.99
    },
    {
        'name': "Sewage Saucy",
        'img': "/static/img/SewageSaucy.png",
        'desc': "Cheese, Pizza sauce",
        'price': 11.99
    },
    {
        'name': "Cheesy Manhole",
        'img': "/static/img/CheesyManhole.png",
        'desc': "Yellow Cheese, Mozzarella, Pepper Cheese, Pizza Sauce",
        'price': 18.99
    },
    {
        'name': "Shroomy Sewage Magic Sewshrooms",
        'img': "/static/img/ShroomySewage.png",
        'desc': "Mushrooms, Chicken, Pepper Cheese, Yellow Cheese, Pizza sauce",
        'price': 19.99
    },
]

def menu_index(request):
    return render(request, 'menu/pizza_menu.html', context={'pizzas': pizzas})

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