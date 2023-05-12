from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_index, name="home-index"),
    path('cart', views.cart_index, name="cart-index"),
    path('cart/<int:typeid>/<int:objectid>', views.add_to_cart_index, name="add-pizza-index"),

    path('offers', views.offers_index, name="offers-index"),

    path('account/', views.account_index, name="account-index"),
    path('account/profile', views.profile_index, name="profile-index"),
    path('account/login', LoginView.as_view(template_name="account/login_screen.html"), name='login'),
    path('account/logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('account/login', views.account_login_index, name="login-index"),
    path('account/create', views.account_create_index, name="create-index"),

    path('custom/create', views.create_pizza_index, name="create-pizza-index"),

    path('menu', views.menu_index, name="menu-index"),
    path('menu/saved', views.menu_index, name="saved-menu-index"),
    path('menu/pizzas', views.menu_index, name="pizza-menu-index"),
    path('menu/drinks', views.menu_index, name="drink-menu-index"),
    path('menu/sides', views.menu_index, name="side-menu-index"),
    path('payment/contact', views.contact_index, name='contact_index'),
    path('payment/payment', views.input_card_info, name='payment_index'),
    path('payment/order_confirm', views.order_confirm_index, name='order_confirm_index'),
    path('payment/payment', views.payment_index, name='payment_index'),
    path('payment/order_confirm', views.order_confirm_index, name='order_confirm_index'),
    #path('menu/Create_Pizza', views.create_pizza, name="create_pizza")
]