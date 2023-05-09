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

sides = [
    {
        'name': 'Sewer Sticks',
        'img': '/static/img/SewerSticks.png',
        'desc': 'Sewer sticks poured in our legendary sewery oil',
        'price': 6.99
    },
    {
        'name': 'Sewer Cheesy Sticks',
        'img': '/static/img/SewerCheesySticks.png',
        'desc': 'Sewer sticks with delicious cheese  in the middle  poured with our legendary sewery oil.',
        'price': 8.99
    },
    {
        'name': 'Spicy Sewer Bread',
        'img': '/static/img/SpicySewerBread.png',
        'desc': 'Our cheesy bread  topped with our wide collection of sewer spices',
        'price': 9.99
    },
    {
        'name': 'Chocolaty Calzone',
        'img': '/static/img/ChocolatyCalzone.png',
        'desc': 'A calzone filled with chocolate and bit of caramel smeared with our legendary sewery oil.',
        'price': 12.99
    },
]

def menu_index(request):
    return render(request, 'menu/pizza_menu.html', context={'pizzas': pizzas})

def drink_index(request):
    return render(request, 'menu/drink_menu.html')

def sides_index(request):
    return render(request, 'menu/side_menu.html', context={'sides': sides})

def create_pizza(request):
    if request.method == 'POST':
        form = create_pizza(data=request.POST)
        if form.is_valid():  pizza = form.save()
        else:
        form = PizzaCreateForm()
    return render(request, 'pizza/create_pizza.html', {
        'form': form
})