from django import template
import markdown
from django.db.models import Count
from django.utils.safestring import mark_safe
from home.models import News, Category, Comment


register  = template.Library()


@register.inclusion_tag('news/navigation.html')
def nav_dynamic():
    categories = Category.objects.all()
    return {'categories':categories}


@register.inclusion_tag('news/last_four.html')
def homepage():
    late_four = News.objects.order_by('-created')[:6]
    return {'latest':late_four}

@register.inclusion_tag('news/latest_news.html')
def sidebar():
    latest_news = News.objects.order_by('-created')[6:14]
    return {'latest_news':latest_news}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.inclusion_tag('news/latest_comments.html')
def latest_com():
    latest_comments = Comment.objects.filter(active=True).order_by('-created')[:4]
    return {'latest_comments':latest_comments}


@register.inclusion_tag('news/most_commented_news.html')
def most_commented():
    most_com = News.objects.annotate(comments=Count('comment')).order_by('-created')[:4]
    return {'most_com':most_com}