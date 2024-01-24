from django.template import Library

from blog.models import Tag


register = Library()

@register.inclusion_tag('blog/search_form_tpl.html')
def show_search_form(text_search=''):
    return {'text_search': text_search}