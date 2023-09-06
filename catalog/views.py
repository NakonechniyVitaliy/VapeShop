from django.shortcuts import render, redirect
from .models import *
from orders.models import Order
from .forms import ProductForm
from .models import Product
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):

    transit_data = dict()
    transit_data['title'] = 'Каталог'
    all_products = Product.objects.all()
    all_category = Category.objects.all()
    all_producer = Producer.objects.all()
    all_orders = Order.objects.filter(user_id=request.user.id)

    products_count = len(all_products)         # Рахуємо кількість об'ектів у кожній моделі
    producer_count = len(all_producer)
    category_count = len(all_category)

    transit_data['all_products'] = all_products
    transit_data['all_categories'] = all_category
    transit_data['all_producers'] = all_producer
    transit_data['user_orders'] = all_orders
    transit_data['products_count'] = len(all_products)
    transit_data['producer_count'] = len(all_producer)
    transit_data['category_count'] = len(all_category)

    transit_data['user_orders']: Order.objects.filter(user_id=request.user.id)

    paginator = Paginator(all_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    transit_data['page_obj'] = page_obj

    return render(request, 'catalog/index.html', context=transit_data)


def create(request):
    transit_data = dict()
    transit_data['app'] = 'Додавання товару'
    transit_data['title'] = 'Каталог'

    transit_data['user_orders']: Order.objects.filter(user_id=request.user.id)

    if request.method == 'GET':
        if request.user.username == 'adminVitalii':
            transit_data['form'] = ProductForm()
            return render(request, 'catalog/create.html', context=transit_data)
        else:
            logout(request)
            return redirect('/accounts/signin')
    elif request.method == 'POST':
        filled_form = ProductForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/catalog/index')


def delete(request, product_id):
    transit_data = dict()
    transit_data['app'] = 'Видалення товару'
    transit_data['title'] = 'Каталог'

    transit_data['user_orders']: Order.objects.filter(user_id=request.user.id)

    target_product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        transit_data['target_product'] = target_product
        return render(request, 'catalog/delete.html', context=transit_data)
    elif request.method == 'POST':
        target_product.delete()
        return redirect('/catalog/index')


def detail(request, product_id):
    transit_data = dict()
    transit_data['title'] = 'Каталог'
    transit_data['app'] = 'про товар'
    transit_data['user_orders']: Order.objects.filter(user_id=request.user.id)

    target_product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        transit_data['target_product'] = target_product
        return render(request, 'catalog/detail.html', context=transit_data)
    elif request.method == 'POST':
        return redirect('/catalog/index')