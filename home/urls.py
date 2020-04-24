from django.contrib.sitemaps.views import sitemap
from django.urls import path
from home.sitemaps import NewsSitemap
from . import views
from about import views as about_views
from contact import views as contact_views
from django.conf import settings
from django.conf.urls.static import static
from .feeds import LatestNewsFeed


sitemaps = {
    'news': NewsSitemap,
}

urlpatterns = [

    path('',views.home,name='home'),


    path('news/<int:year>/<int:month>/<int:day>/<slug:slug>/',views.news_detail,name='news-detail'),
    path('news/category/<str:category>/',views.category_list,name='category-list'),

    path('news/all/',views.news_list,name='news-list'),
    path('news/all/<slug:tag_slug>/',views.news_list,name='news-bt-tag'),

    # contact and about
    path('contact/',contact_views.contact,name='contact'),
    path('about/',about_views.about,name='about'),

    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('feed/',LatestNewsFeed(),name='news-feed'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)