from django.template import Library
from products.models import category
from django.shortcuts import get_object_or_404

register = Library()

@register.simple_tag
def get_categories():
    return category.objects.filter(parent= None)

@register.simple_tag
def get_sub_categorys(id):
    categorys = category.objects.filter(parent__id=id)
    return categorys