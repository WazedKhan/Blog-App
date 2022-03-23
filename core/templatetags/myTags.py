from django import template

register = template.Library()

@register.filter
def lower(value):
    return value.lower()+" ok its working"

@register.filter
def module(number,value):
    return number % value