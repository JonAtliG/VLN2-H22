from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Pizza, User, Side, Drink, Cart, Offer3For2
from core.forms.pizza_form import PizzaCreateForm
from core.forms.user_form import Create_Account_Form, ProfileForm
from core.forms.payment_form import PaymentForm
import json


def __get_menu_json_object(pizza_query, side_query, drink_query, user_pizza_query, offer_id=None):
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
                'active_offer': offer_id
            }
        ]
    )
    return json_data

def __get_pizza_price_and_description(pizza):
    topping_list = []
    pizza_toppings = pizza.toppings()
    keys = ['Bacon', 'Chicken', 'Ham', 'Pepperoni', 'Jalapeno', 'Mushrooms', 'Onion', 'Paprika',
            'Pineapple', 'Cheese', 'Mozzarella', 'Pepper_Cheese', 'Yellow_Cheese', 'Pizza_Sauce']
    for key in keys:
        if pizza_toppings[key]:
            topping_list.append(key.replace("_", " "))
    if len(topping_list) > 1:
        desc = ", ".join(topping_list[:-1])+ " and " + topping_list[-1]
    else:
        desc = "" if len(topping_list) == 0 else topping_list[0]
    price = 6.99 + len(topping_list)
    return desc, price




def account_index(request):
    if request.user.is_authenticated:
        return redirect('profile-index')
    return render(request, 'account/account.html')


def profile_index(request):
    profile_man = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(instance=profile_man, data=request.POST)
        if form.is_valid():
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
            print(2)
            form.save()
            return redirect('order_confirm_index')
        else:
            print(form.errors)
    form = PaymentForm()
    form.set_user(request.user.id)
    return render(request, 'payment/payment.html', {
        'form': form
    })


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


def menu_select_offer_index(request, offerid):
    if request.user.is_authenticated:
        user_pizzas = Pizza.objects.all().filter(User=request.user)
    else:
        user_pizzas = []
    pizzas = Pizza.objects.all().filter(User__isnull=True)
    context_data = __get_menu_json_object(pizza_query=pizzas,
                                          side_query=[],
                                          drink_query=[],
                                          user_pizza_query=user_pizzas,
                                          offer_id=offerid,)
    return render(request, 'menu/3_for_2_menu.html', context={'data': context_data})


@login_required(login_url='login-index')
def cart_index(request):
    cart = Cart.objects.all().filter(user_id=request.user.id)
    items = []
    for item in cart:
        if item.pizza_id is not None:
            pizza = Pizza.objects.get(pk=item.pizza_id)
            desc, price = __get_pizza_price_and_description(pizza)
            items.append({'name': pizza.name, 'desc': desc, 'price': price})
        elif item.side_id is not None:
            side = Side.objects.get(pk=item.side_id)
            items.append({'name': side.name, 'desc': side.desc, 'price': side.price})
        elif item.drink_id is not None:
            drink = Drink.objects.get(pk=item.drink_id)
            items.append({'name': drink.name, 'desc': drink.desc, 'price': drink.price})
        else:
            offer = Offer3For2.objects.get(pk=item.offer_3_for_2_id)
            pizza1 = Pizza.objects.get(pk=offer.pizza1_id)
            pizza2 = Pizza.objects.get(pk=offer.pizza1_id)
            pizza3 = Pizza.objects.get(pk=offer.pizza1_id)
            items.append({'name': "3 for 2 offer", 'desc': f"{pizza1.name}, {pizza2.name}, {pizza3.name}", 'price': 34.99})
    return render(request, 'cart.html', context={'data': items})


@login_required(login_url='login-index')
def add_to_cart_index(request, typeid, objectid):
    print(objectid)
    if typeid == 0:
        cart_item = Cart(user_id=request.user.id, pizza_id=objectid)
    elif typeid == 1:
        cart_item = Cart(user_id=request.user.id, side_id=objectid)
    else:
        cart_item = Cart(user_id=request.user.id, drink_id=objectid)
    cart_item.save()
    return redirect('menu-index')


@login_required(login_url='login-index')
def add_offer_to_cart_index(request, pizza1id, pizza2id, pizza3id):
    offer = Offer3For2()
    offer.user_id = request.user.id
    offer.pizza1_id = pizza1id
    offer.pizza2_id = pizza2id
    offer.pizza3_id = pizza3id
    offer.save()
    cart = Cart(user_id=request.user.id, offer_3_for_2_id=offer.id)
    cart.save()
    return redirect('cart-index')


def home_index(request):
    return render(request, 'home.html')


# def create_pizza(request):

def contact_index(request):
    return render(request, 'payment/contact.html')

def payment_index(request):
    return render(request, 'payment/payment.html')


def order_confirm_index(request):
    Cart.objects.all().filter(user_id=request.user.id).delete()
    Offer3For2.objects.all().filter(user_id=request.user.id).delete()
    return render(request, 'payment/order_confirm.html')


