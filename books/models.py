from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.title} - by {self.author}'
    