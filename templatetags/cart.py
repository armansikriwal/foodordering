from django import template
register=template.Library()

@register.filter("is_in_cart")
def is_in_cart(product):
    return True
    