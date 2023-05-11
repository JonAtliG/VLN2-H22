from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_index, name="home-index"),
    path('cart', views.cart_index, name="cart-index"),

    path('offers', views.offers_index, name="offers-index"),

    path('account/', views.account_index, name="account-index"),
    path('account/profile', views.profile_index, name="profile-index"),
    path('account/login', LoginView.as_view(template_name="account/login_screen.html"), name='login'),
    path('account/logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('account/login', views.account_login_index, name="login-index"),
    path('account/create', views.account_create_index, name="create-index"),

    path('custom/create', views.create_pizza_index, name="create-pizza-index"),

    path('menu', views.menu_index, name="menu-index"),
    path('menu/saved', views.saved_menu_index, name="saved-menu-index"),
    path('menu/pizzas', views.pizza_menu_index, name="pizza-menu-index"),
    path('menu/drinks', views.drink_menu_index, name="drink-menu-index"),
    path('menu/sides', views.side_menu_index, name="side-menu-index"),
    #path('menu/Create_Pizza', views.create_pizza, name="create_pizza")
]