from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.core.mail import send_mail
from .models import Order


def index(request):

    return render(request, 'orders/index.html', {
        'title': 'Кошик',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })


def bill(request, sel_list: str):                       # '1,2,37000'
    sel_list_str = sel_list.split(',')                  # ['1', '2', '37000']
    sel_list_num = [int(x) for x in sel_list_str[:-1]]  # [1, 2] Вказує ID товарів
    total_price = int(sel_list_str[-1])                 # 37000
    final_list = []
    #
    for order_id in sel_list_num:
        order = Order.objects.get(id=order_id)
        final_list.append({
            'product_name': order.product.name,
            'category_name': order.product.category.name,
            'product_price': order.product.price,
            'product_photo': order.product.photo
        })
    return render(request, 'orders/bill.html', {
        'title': 'Кошик',
        'app': 'Оформлення замовлення',
        'total_price': total_price,
        'final_list': final_list,
        'init_list': sel_list,
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })


def confirm(request, init_list: str):
    if request.method == 'GET':
        return render(request, 'orders/confirm.html', {
            'title': 'Кошик',
            'page': 'Підтвердження замовлення',
            'app': 'Оформлення замовлення',
            'init_list': init_list
        })
    elif request.method == 'POST':
        email = request.POST.get('email')
        #
        sel_list_str = init_list.split(',')
        sel_list_num = [int(x) for x in sel_list_str[:-1]]
        total_price = int(sel_list_str[-1])
        info_list = []
        #
        for order_id in sel_list_num:
            order = Order.objects.get(id=order_id)
            info_list.append({
                'product_name': order.product.name,
                'category_name': order.product.category.name,
                'product_price': order.product.price,
                'user_orders': Order.objects.filter(user_id=request.user.id)
            })
        #
        subject = 'Повідомлення про замовлення на сайті SoskaVapeShop'
        body = f'''
            <h1>{subject}</h1>
            <hr/>
            <h2 style="color: purple">
                Ви підтвердили замовлення наступних товарів
            </h2>
            <h3>
            <ol>
        '''
        for item in info_list:
            body += f'''
                <li>
                    {item.get('product_name')} / 
                    {item.get('category_name')} -
                    {item.get('product_price')} грн
                </li>
            '''
        body += f'''
            </ol>
            </h3>
            <hr/>
            <h2>
                Загальна сума до сплаты:
                <span style="color: red">
                    {total_price} грн 
                </span>
            </h2>
        '''
        #
        success = send_mail(subject, '', 'soska-vape-shop@gmail.com', [email],
                            fail_silently=False, html_message=body)
        if success:
            return render(request, 'orders/thanks.html', {
                'title': 'Подяка за замовлення',
                'email': email
            })
        else:
            return render(request, 'orders/failed.html', {
                'title': 'Помилка поштового відправлення',
                'page': 'failed',
                'app': 'orders'
            })


def ajax_cart(request):
    response = dict()
    response['message'] = 'Привіт від сервера!'

    # 1 - Отримуємо значення GET-параметрів від клієнта:
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    price = request.GET.get('price')

    # 2 - Створюємо нове замовлення та зберігаємо його в БД:
    Order.objects.create(
        title=f'Order-{pid}/{uid}/{timezone.now()}',
        user_id=uid,
        product_id=pid,
        amount=float(price),
        notes='Очікує підтвердження'
    )

    # 3 - Зчитуємо із бази список всіх замовлень даного користувача:
    user_orders = Order.objects.filter(user_id=uid)

    # 4 - Обчислюємо загальну вартість всіх замовлень даного користувача:
    amount = 0
    for order in user_orders:
        amount += order.amount

    # 5 - Записуємо у відповідь сервера загальну вартість та кількість товарів:
    response['amount'] = amount
    response['count'] = len(user_orders)

    return JsonResponse(response)


def ajax_cart_display(request):
    # 1
    response = dict()
    response['message'] = 'AJAX-cart_display-OK'

    # 2
    uid = request.GET.get('uid')
    response['uid'] = uid

    # 3
    user_products = Order.objects.filter(user_id=uid)
    amount = 0

    # 4
    for product in user_products:
        amount += product.amount

    # 5
    response['count'] = len(user_products)
    response['total'] = amount

    return JsonResponse(response)


def order_delete(request):
    response = dict()
    response['message'] = 'Привіт від сервера!'

    oid = request.GET.get('oid')
    uid = request.GET.get('uid')

    Order.objects.filter(id=oid).delete()






    # Удаление всех ордеров юзера
    # oid = request.GET.get('oid')
    # uid = request.GET.get('uid')
    # user_orders = Order.objects.filter(user_id=uid)
    # user_orders.delete(),


    # target_order = Order.objects.get(order_id=oid),
    # target_order.delete(),

