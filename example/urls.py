# example/urls.py
from django.urls import path

from example.views import index, bootstrap


urlpatterns = [
    path("", index),
    path("bootstrap", bootstrap),
]
