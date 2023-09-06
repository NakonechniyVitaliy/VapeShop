from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_cart),
    path('order_delete', order_delete),
    path('ajax_cart_display', ajax_cart_display),
    re_path(r'^bill/(?P<sel_list>[0-9\,]+)$', bill),
    re_path(r'^confirm/(?P<init_list>[0-9\,]+)$', confirm)
]
