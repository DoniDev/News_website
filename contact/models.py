from django.db import models


class Contact(models.Model):
     address = models.CharField(max_length=100)
     phone = models.CharField(max_length=17)
     email = models.EmailField(default=1)


     def __str__(self):
         return f'Owners details {self.id}'
