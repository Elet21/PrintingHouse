from django.urls import path
from .views import CreatOrder


urlpatterns = [
    path('create-order/', CreatOrder.as_view(), name='create_order')
]