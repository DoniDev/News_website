from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name



class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='pics',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = TaggableManager()



    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('news-detail',
            args=[
                self.created.year,
                self.created.month,
                self.created.day,
                self.slug
        ])


    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 1335 or img.width > 2000:
            output_size = (1335,2000)
            img.thumbnail(output_size)
            img.save(self.image.path)

























class Comment(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    message = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}\'s comment on {self.news.title}'

    class Meta:
        verbose_name_plural = 'Comments'