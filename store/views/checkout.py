from django.shortcuts import render, redirect
from django.views import View


class CheckOut(View):
    def post(self, request):
        pass
        request.session['cart'] = {}
        return redirect('cart')
