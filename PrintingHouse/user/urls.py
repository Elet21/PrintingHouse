from django.urls import path
from .views import Register, my_logout, CustomLoginView, cart


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('logout/', my_logout, name='logout_url'),
    path('accounts/login/', CustomLoginView.as_view(), name='login_user'),
    path('cart/', cart, name='cart'),
]