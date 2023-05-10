from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="offers-index"),
    path('pizzas', views.all_pizzas, name="all-pizzas")
]
