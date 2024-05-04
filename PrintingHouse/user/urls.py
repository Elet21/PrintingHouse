from django.urls import path
from .views import Register, my_logout, CustomLoginView


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('logout/', my_logout, name='logout_url'),
    path('login/', CustomLoginView.as_view(), name='login')
    # path('logout/', views.LogoutView.as_view(), name='logout'),
]