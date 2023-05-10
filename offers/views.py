from django.shortcuts import render
from offers.models import Pizza
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'special_offer.html')

def all_pizzas(request):
    pizzas = Pizza.objects.all().values()
    qs_json = serializers.serialize('json', pizzas)
    return HttpResponse(qs_json)



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
