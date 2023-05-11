from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Pizza, User, Side, Drink
from core.forms.pizza_form import PizzaCreateForm
from core.forms.user_form import Create_Account_Form, ProfileForm


def __get_pizza_list(queryset):
    pizza_list = []
    for i, pizza in enumerate(queryset):
        pizza_list.append({'id': pizza['id']})
        pizza_list[i]['name'] = pizza['name']
        pizza_list[i]['img'] = pizza['img']

        toppings = []
        for topping in pizza.keys():
            if pizza[topping] is True:
                toppings.append(topping.replace("_", " "))
        if len(toppings) > 1:
            pizza_list[i]['desc'] = f"{', '.join(toppings[:-1])} and  {toppings[-1]}"
        else:
            pizza_list[i]['desc'] = "" if len(toppings) == 0 else toppings[1]
        pizza_list[i]['price'] = round(10.99 + len(toppings), 2)
    return pizza_list


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
            if request.user.id == form['User']:
                form.save()
                return redirect('saved-menu-index')
    form = PizzaCreateForm()
    form.set_user(request.user.id)
    return render(request, 'menu/create_pizza.html', {
        'form': form
    })


@login_required(login_url='login-index')
def saved_menu_index(request):
    pizza_list = __get_pizza_list(Pizza.objects.filter(User=request.user).values())
    return render(request, 'menu/menu.html', context={'data': {'pizzas': pizza_list}})


def menu_index(request):
    pizza_list = __get_pizza_list(Pizza.objects.all().filter(User__isnull=True).values())
    side_object = Side.objects.all().values('name', 'img', 'desc', 'price')
    drink_object = Drink.objects.all().values('name', 'img', 'desc', 'price')
    return render(request, 'menu/menu.html', context={'data': {'pizzas': pizza_list,
                                                               'sides': side_object,
                                                               'drinks': drink_object}})


def pizza_menu_index(request):
    pizza_list = __get_pizza_list(Pizza.objects.all().filter(User__isnull=True).values())
    return render(request, 'menu/menu.html', context={'data': {'pizzas': pizza_list}})


def side_menu_index(request):
    side_object = Side.objects.all().values('name', 'img', 'desc', 'price')
    return render(request, 'menu/menu.html', context={'data': {'sides': side_object}})


def drink_menu_index(request):
    drink_object = Drink.objects.all().values('name', 'img', 'desc', 'price')
    return render(request, 'menu/menu.html', context={'data': {'drinks': drink_object}})

def cart_index(request):
    return render(request, 'cart.html')


def home_index(request):
    return render(request, 'home.html')

def contact_index(request):
    return render(request, 'payment/contact.html')

def payment_index(request):
    return render(request, 'payment/payment.html')


#def create_pizza(request):
#    if request.method == 'POST':
#        form = create_pizza(data=request.POST)
#        if form.is_valid():
#            pizza = form.save()
#        else:
#            form = PizzaCreateCustom()
#    return render(request, 'pizza/create_pizza.html', {
#        'form': form
#})