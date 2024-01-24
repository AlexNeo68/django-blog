from django.template import Library

from blog.models import Tag


register = Library()

@register.inclusion_tag('blog/tags_cloud_tpl.html')
def show_tags_cloud(cnt=3):
    tags = Tag.objects.all()
    return {'tags': tags}