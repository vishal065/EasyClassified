from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get('FirstName')
        last_name = post_data.get('LastName')
        phone = post_data.get('Phone')
        email = post_data.get('email')
        password = post_data.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_msg = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        if not error_msg:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

        error_msg = self.validate_customer(customer)

        data = {
            'error': error_msg,
            'values': value
        }
        return render(request, 'signup.html', data)

    def validate_customer(self, customer):

        error_msg = None
        if not customer.first_name:
            error_msg = 'This First name Required'
        elif len(customer.first_name) < 4:
            error_msg = 'Name should be greater then 4 char'
        elif customer.is_exist():
            error_msg = 'Email Already exist'

        return error_msg
