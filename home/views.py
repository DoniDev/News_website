from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import RedirectView
from taggit.models import Tag
from home.forms import CommentForm
from . models import *


def home(request):

    return render(request,'news/home.html')

@login_required(login_url='login')
def news_detail(request,year,month,day,slug):
    news = get_object_or_404(News,created__year=year,created__month=month,created__day=day,slug=slug)
    related = News.objects.filter(category__name=news.category).exclude(id=news.id).order_by('-created')[0:2]
    comments = news.comment_set.filter(active=True)
    comment_count = news.comment_set.count()
    tags = news.tags.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            messages.success(request,'Comment added succesfully')

    else:
        comment_form = CommentForm()

    context={
        'news':news,
        'related':related,
        'comments':comments,
        'comment_form':comment_form,
        'comment_count':comment_count,
        'tags':tags,


    }

    return render(request,'news/news_detail.html',context=context)




def category_list(request,category,tag_slug=None):
    news_list = News.objects.filter(category__name=category).order_by('-created')
    category = Category.objects.get(name=category)
    tag=None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        news_list.filter(tags__in=[tag])

    paginator = Paginator(news_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context={
        'news_list':news_list,
        'page_obj':page_obj,
        'tag':tag,
        'category':category,
    }

    return render(request, 'news/category_list.html', context=context)

def news_list(request,tag_slug=None):
    object_list = News.objects.all().order_by('-created')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list,5)
    page_number = request.GET.get('page')
    try:
        news_all = paginator.page(page_number)
    except PageNotAnInteger:
        news_all = paginator.page(1)
    except EmptyPage:
        news_all = paginator.page(paginator.num_pages)

    context={
        'news_all':news_all,
        'page_number':page_number,
        'tag':tag,
    }
    return render(request,'news/news_all.html',context=context)


