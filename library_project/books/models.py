from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13,unique=True)
    def __str__(self):
        return self.title