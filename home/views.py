from django.shortcuts import render
from orders.models import Order
from django.contrib.auth import logout
from .forms import NewProductForm
from .models import NewProduct
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'home/index.html', {
        'title': 'Головна',
        'page': 'index',
        'app': 'home',
        'user_orders': Order.objects.filter(user_id=request.user.id),
        'all_new_product': NewProduct.objects.all()
    })


def about(request):
    return render(request, 'home/about.html', {
        'title': 'Про сайт',
        'page': 'about',
        'app': 'home'
    })


def contacts(request):
    return render(request, 'home/contacts.html', {
        'title': 'Контакти',
        'page': 'contacts',
        'app': 'home'
    })


def delete(request, product_id):
    transit_data = dict()
    transit_data['app'] = 'Видалення товару'
    transit_data['title'] = 'Домашня'

    new_target_product = NewProduct.objects.get(id=product_id)
    if request.method == 'GET':
        transit_data['new_target_product'] = new_target_product
        return render(request, 'home/delete.html', context=transit_data)
    elif request.method == 'POST':
        new_target_product.delete()
        return redirect('/')


def create(request):
    transit_data = dict()
    transit_data['app'] = 'Додавання товару'
    transit_data['title'] = 'Домашня'

    if request.method == 'GET':
        if request.user.username == 'adminVitalii':
            transit_data['form'] = NewProductForm()
            return render(request, 'home/create.html', context=transit_data)
        else:
            logout(request)
            return redirect('/accounts/signin')
    elif request.method == 'POST':
        filled_form = NewProductForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/')

