from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag
from home.forms import CommentForm
from . models import *
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from . forms import SearchForm
from django.contrib.postgres.search import  TrigramSimilarity


def home(request):

    query = None
    results =[]
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title','body')
            search_query = SearchQuery(query)
            results = News.objects.annotate(search= search_vector,rank=SearchRank(search_vector,search_query))\
                .filter(search=search_query).order_by('-rank')



            # results = News.objects.annotate(similarity=TrigramSimilarity('title',query),)\
            #     .filter(similarity__gte=0.1).order_by('-similarity')

    else:
        form = SearchForm()

    context={
        'form':form,
        'query':query,
        'results':results,
    }
    return render(request,'news/home.html',context=context)



@login_required(login_url='login')
def news_detail(request,year,month,day,slug):
    news = get_object_or_404(News,created__year=year,created__month=month,created__day=day,slug=slug)
    related = News.objects.filter(category__name=news.category).exclude(id=news.id).order_by('-created')[0:2]
    comments = news.comment_set.filter(active=True)
    comment_count = news.comment_set.count()
    tags = news.tags.all()

    query = None
    results = []
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = News.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)) \
                .filter(search=search_query).order_by('-rank')

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
        'results':results,
        'query':query,
        'form':form,


    }

    return render(request,'news/news_detail.html',context=context)




def category_list(request,category,tag_slug=None):
    news_list = News.objects.filter(category__name=category).order_by('-created')
    category = Category.objects.get(name=category)
    tag=None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        news_list.filter(tags__in=[tag])

    query = None
    results = []
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = News.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)) \
                .filter(search=search_query).order_by('-rank')

    paginator = Paginator(news_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context={
        'news_list':news_list,
        'page_obj':page_obj,
        'tag':tag,
        'category':category,
        'results':results,
        'query':query,
        'form':form,
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

    query = None
    results = []
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = News.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)) \
                .filter(search=search_query).order_by('-rank')

    context={
        'news_all':news_all,
        'page_number':page_number,
        'tag':tag,
        'results':results,
        'query':query,
        'form':form,
    }
    return render(request,'news/news_all.html',context=context)








