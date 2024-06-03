from django.urls import path
from .views import CreatOrder, order_list, download_pdf


urlpatterns = [
    path('create-order/', CreatOrder.as_view(), name='create_order'),
    path('orders/', order_list, name='order_list'),
    path('order/<int:order_id>/download/', download_pdf, name='download_pdf'),

]