from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Pizza, User, Side, Drink
from core.forms.pizza_form import PizzaCreateForm
from core.forms.user_form import Create_Account_Form, ProfileForm
from core.forms.payment_form import PaymentForm
import json


def __get_menu_json_object(pizza_query, side_query, drink_query, user_pizza_query):
    json_data = json.dumps(
        [
            {
                'pizzas': [
                    {
                        'id': pizza.id,
                        'name': pizza.name,
                        'img': pizza.img,
                        'toppings': {
                            'Bacon': pizza.Bacon,
                            'Chicken': pizza.Chicken,
                            'Ham': pizza.Ham,
                            'Pepperoni': pizza.Pepperoni,
                            'Jalapeno': pizza.Jalapeno,
                            'Mushrooms': pizza.Mushrooms,
                            'Onion': pizza.Onion,
                            'Paprika': pizza.Paprika,
                            'Pineapple': pizza.Pineapple,
                            'Cheese': pizza.Cheese,
                            'Mozzarella': pizza.Mozzarella,
                            'Pepper_Cheese': pizza.Pepper_Cheese,
                            'Yellow_Cheese': pizza.Yellow_Cheese,
                            'Pizza_Sauce': pizza.Pizza_Sauce,
                        }
                    } for pizza in pizza_query
                ],
                'user_pizzas': [
                    {
                        'id': pizza.id,
                        'name': pizza.name,
                        'img': pizza.img,
                        'toppings': {
                            'Bacon': pizza.Bacon,
                            'Chicken': pizza.Chicken,
                            'Ham': pizza.Ham,
                            'Pepperoni': pizza.Pepperoni,
                            'Jalapeno': pizza.Jalapeno,
                            'Mushrooms': pizza.Mushrooms,
                            'Onion': pizza.Onion,
                            'Paprika': pizza.Paprika,
                            'Pineapple': pizza.Pineapple,
                            'Cheese': pizza.Cheese,
                            'Mozzarella': pizza.Mozzarella,
                            'Pepper_Cheese': pizza.Pepper_Cheese,
                            'Yellow_Cheese': pizza.Yellow_Cheese,
                            'Pizza_Sauce': pizza.Pizza_Sauce,
                        }
                    } for pizza in user_pizza_query
                ],
                'sides': [
                    {
                        'id': side.id,
                        'name': side.name,
                        'img': side.img,
                        'desc': side.desc,
                        'price': side.price
                    } for side in side_query
                ],
                'drinks': [
                    {
                        'id': drink.id,
                        'name': drink.name,
                        'img': drink.img,
                        'desc': drink.desc,
                        'price': drink.price
                    } for drink in drink_query
                ],
            }
        ]
    )
    return json_data


def account_index(request):
    if request.user.is_authenticated:
        return redirect('profile-index')
    return render(request, 'account/account.html')


def profile_index(request):
    profile_man = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(instance=profile_man, data=request.POST)
        if form.is_valid():
            for f in form:
                print(f.name, f.value())
            profile_man.save()
            return redirect('menu-index')
    form = ProfileForm(instance=profile_man)
    return render(request, 'account/account.html', {
        'form': form
    })


def account_login_index(request):
    return render(request, 'account/login_screen.html')


def account_create_index(request):
    if request.method == 'POST':
        form = Create_Account_Form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-index')
    return render(request, 'account/create_account.html', {
        'form': Create_Account_Form()
    })


def offers_index(request):
    return render(request, 'special_offer.html')


@login_required(login_url='login-index')
def create_pizza_index(request):
    if request.method == 'POST':
        form = PizzaCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('saved-menu-index')
    form = PizzaCreateForm()
    form.set_user(request.user.id)
    return render(request, 'menu/create_pizza.html', {
        'form': form
    })


def input_card_info(request):
    if request.method == 'POST':
        form = PaymentForm(data=request.POST)
        print(form['User'].value())
        if form.is_valid():
            form.save()
            return redirect('order_confirm_index')
    form = PaymentForm()
    form.set_user(request.user.id)
    print(form['User'].value())
    print(request.user.id)
    return render(request, 'payment/payment.html', {
        'form': form
    })

#@login_required(login_url='login-index')
#def saved_menu_index(request):
#    pizza_list = __get_pizza_list(Pizza.objects.filter(User=request.user).values())
#    return render(request, 'menu/menu.html', context={'data': {'pizzas': pizza_list}})


def menu_index(request):
    if request.user.is_authenticated:
        user_pizzas = Pizza.objects.all().filter(User=request.user)
    else:
        user_pizzas = []
    pizzas = Pizza.objects.all().filter(User__isnull=True)
    sides = Side.objects.all()
    drinks = Drink.objects.all()
    context_data = __get_menu_json_object(pizza_query=pizzas,
                                          side_query=sides,
                                          drink_query=drinks,
                                          user_pizza_query=user_pizzas)
    return render(request, 'menu/menu.html', context={'data': context_data})


#def pizza_menu_index(request):
#    # pizza_list = __get_pizza_list(Pizza.objects.all().filter(User__isnull=True).values())
#    data = __get_menu_json_object(pizza_query=Pizza.objects.all().filter(User__isnull=True))
#    return render(request, 'menu/menu.html', context={'data': data})
#
#
#def side_menu_index(request):
#    side_object = Side.objects.all().values('name', 'img', 'desc', 'price')
#    return render(request, 'menu/menu.html', context={'data': {'sides': side_object}})
#
#
#def drink_menu_index(request):
#    drink_object = Drink.objects.all().values('name', 'img', 'desc', 'price')
#    return render(request, 'menu/menu.html', context={'data': {'drinks': drink_object}})


def cart_index(request):
    return render(request, 'cart.html')


def home_index(request):
    return render(request, 'home.html')


# def create_pizza(request):

def contact_index(request):
    return render(request, 'payment/contact.html')

def payment_index(request):
    return render(request, 'payment/payment.html')


def order_confirm_index(request):
    return render(request, 'payment/order_confirm.html')



#def create_pizza(request):
#    if request.method == 'POST':
#        form = create_pizza(data=request.POST)
#        if form.is_valid():
#            pizza = form.save()
#        else:
#            form = PizzaCreateCustom()
#    return render(request, 'pizza/create_pizza.html', {
#        'form': form
# })
