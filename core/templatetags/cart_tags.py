from django import template
from sympy import ordered
from core.models import Order,OrderItem,Item,Brand


register=template.Library()


@register.filter
def count_total_items(user):
    if user.is_authenticated:
        qt = Order.objects.filter(
            user=user,
            ordered=False
        )
        if qt.exists():
            return qt[0].items.count()
    return 0
@register.filter()
def get_quantity(user):
    if user.is_authenticated:
        order = Brand.objects.all().count()
        return order
    return "none"