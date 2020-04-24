from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from . models import News


class LatestNewsFeed(Feed):
    title = 'News Website'
    link = reverse_lazy('news-list')
    description = 'New content of the website'

    def items(self):
        return News.objects.all().order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body,30)

