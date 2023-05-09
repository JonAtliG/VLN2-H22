from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_index, name="menu-index"),
    path('pizzas', views.menu_index, name="menu-index"),
    path('drinks', views.drink_index, name="drink-index"),
    path('sides', views.sides_index, name="side-index"),
    path('Create_Pizza', views.create_pizza, name="create_pizza")
    ]
