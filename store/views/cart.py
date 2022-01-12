from django.shortcuts import render
from django.views import View
from store.models.Product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id_in_cart(ids)
        return render(request, 'cart.html', {'cart_product': products})
