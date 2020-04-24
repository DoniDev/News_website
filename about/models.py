from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class Statistics(models.Model):
    title = models.CharField(max_length=100)
    amount = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Statictics'

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team',default='default.jpg')

    class Meta:
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.name
