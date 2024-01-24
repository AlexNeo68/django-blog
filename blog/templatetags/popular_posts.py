from django.template import Library

from blog.models import Post

register = Library()

@register.inclusion_tag('blog/popular_posts_tpl.html')
def show_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}