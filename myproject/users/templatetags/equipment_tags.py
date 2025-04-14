from django import template
from users.models import Category, Tag, Messages, Comments, Journal

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all() 

@register.simple_tag()
def get_tags():
    return Tag.objects.all()

@register.simple_tag()
def get_input_messages(owner):
    return  Messages.objects.filter(owner=owner).count()

@register.simple_tag()
def get_output_messages(sender):
    return  Messages.objects.filter(sender=sender).count()

@register.simple_tag()
def get_count_comments(user):
    return  Comments.objects.filter(user=user).count()

@register.simple_tag()
def get_count_journals(user):
    return  Journal.objects.filter(user=user).count()

@register.simple_tag()
def get_count_all_journals():
    return  Journal.objects.count()

@register.simple_tag()
def get_count_all_comments():
    return  Comments.objects.count()