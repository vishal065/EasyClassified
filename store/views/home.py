from django.shortcuts import render, redirect
from store.models.Product import Product
from store.models.category import Category
from django.views import View


# for checking password
# print(make_password('1234'))
# print(check_password('1234', 'pbkdf2_sha256$260000$e1A92jo9DWLQajBdWt0sCh$L8fQTZb9Mp25UcNvUVIrLMf9zr2t/Z5Eq9ofEqj6fQY='))


# Create your views here.
class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = None
        products = Product.get_all_products()
        categories = Category.get_all_categories()

        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            Product.get_all_products()
        data = {}
        data['product_list'] = products
        data['category_list'] = categories
        print(request.session.get('email'))
        return render(request, 'index.html', data)

    def post(self, request):
        # product_from_html it gives product id from index.html name="{{product_from_html.id}}"
        product = request.POST.get('product')
        remove = request.POST.get('remove')  # name ="remove" in html
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')

#
#
#
# def validate_customer(customer):
#     error_msg = None
#     if not customer.first_name:
#         error_msg = 'This First name Required'
#     elif len(customer.first_name) < 4:
#         error_msg = 'Name should be greater then 4 char'
#     elif customer.is_exist():
#         error_msg = 'Email Already exist'
#
#     return error_msg


#
# def register_user(request):
#     post_data = request.POST
#     first_name = post_data.get('FirstName')
#     last_name = post_data.get('LastName')
#     phone = post_data.get('Phone')
#     email = post_data.get('email')
#     password = post_data.get('password')
#     # validation
#     value = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'phone': phone,
#         'email': email
#     }
#     error_msg = None
#     customer = Customer(first_name=first_name,
#                         last_name=last_name,
#                         phone=phone,
#                         email=email,
#                         password=password)
#     if not error_msg:
#         print(first_name, last_name, phone, email, password)
#         customer.password = make_password(customer.password)
#         customer.register()
#         return redirect('homepage')
#
#     error_msg = validate_customer(customer)
#
#     data = {
#         'error': error_msg,
#         'values': value
#     }
#     return render(request, 'signup.html', data)


#       saving
#
# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return register_user(request)

#
# class Login(View):
#     def get(self, request):
#         if request.method == 'GET':
#             return render(request, 'login.html')
#
#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_message = 'Email or Password invalid!!!'
#         else:
#             error_message = 'Email or Password invalid!!!'
#         print(email, password)
#         return render(request, 'login.html', {'error': error_message})
