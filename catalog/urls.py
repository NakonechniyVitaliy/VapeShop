from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('index', index),
    path('create', create),
    re_path(r'^delete/(?P<product_id>[0-9]+)$', delete),
    re_path(r'^detail/(?P<product_id>[0-9]+)$', detail),
]
