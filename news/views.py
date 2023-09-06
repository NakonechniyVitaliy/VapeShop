from django.shortcuts import render
from orders.models import Order


def index(request):
    return render(request, 'news/index.html', {
        'title': 'Новини',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })


