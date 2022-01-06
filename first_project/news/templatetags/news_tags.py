from django import template
from django.db.models import Count, F

from ..models import Category

register = template.Library()


@register.simple_tag(name="get_list_categories")  # параметр name - изменение имени функции
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(Count('news')).filter(news__count__gt=0)
    categories = Category.objects.annotate(Count('news')).filter(news__count__gt=0)
    return {'categories': categories}
