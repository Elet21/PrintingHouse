from django.urls import path

from .views import kazan, chelny


urlpatterns = [
    path('Kazan', kazan, name='kazan'),
    path('Chelny', chelny, name='chelny'),
]