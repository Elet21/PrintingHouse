from django import template
from cart.models import Cart



register = template.Library()


@register.simple_tag()
def user_cart(requests):
    return Cart.objects.filter(user=requests.user)
