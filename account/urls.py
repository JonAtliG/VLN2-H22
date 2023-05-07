from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="account-index"),
    path('login', views.login_index, name="login-index"),
    path('create', views.create_index, name="create-index"),
]
