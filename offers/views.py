from django.shortcuts import render
from offers.models import pizza
from offers.models import topping
# Create your views here.

def index(request):
    return render(request, 'special_offer.html')

def all_pizzas(request):
    qs = pizza.objects.prefetch_related('toppings')
    print()
    for p in pizzas:
        print(p[0], p[1], )
    print(pizzas)

    #for p in pizzas:
    #    topping_ids = on_pizza.objects.filter(pizza_id=p.id)
#
    #    pizza_list.append({
    #        'name': p.name,
    #        'img': p.img,
    #        'desc': ""
    #    })
    #for i in pizza_list:
    #    print(i)
    return render(request, 'special_offer.html', context={'pizzas': pizzas})
