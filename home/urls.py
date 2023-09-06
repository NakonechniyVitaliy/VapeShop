from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('about', about),
    path('contacts', contacts),
    path('create', create),
    re_path(r'^delete/(?P<product_id>[0-9]+)$', delete),
]