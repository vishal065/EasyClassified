from django.contrib import admin
from django.urls import path
from .views import signup, home, cart
from .views.login import Login, logout
from .views.checkout import CheckOut


urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    # path('signup', signup),       old when using function
    path('signup', signup.SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),

]
