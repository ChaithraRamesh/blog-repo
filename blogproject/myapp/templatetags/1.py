from django import template
from myapp.models import Post
register=template.Library()
@register.simple_tag
def total_posts():
	return Post.objects.count()