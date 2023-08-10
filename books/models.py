import self as self
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=11)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('FINANCE', 'Finance'),
        ('POLITICS', 'Politics'),
        ('ROMANCE', 'Romance')
    ]
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=8)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateTimeField(blank=True, null=True)
    copies = models.IntegerField()

    def __str__(self):
        return f"{self.title}{self.isbn}"

    class Meta:
        ordering = ['-title']


class Address(models.Model):
    number = models.PositiveIntegerField()
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=75)
    country =models.CharField(max_length=100, default="Nigeria")


class BookInstance(models.Model):
    book = models.OneToOneField(Book, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_borrowed = models.DateField(auto_now_add=True)
    date_returned = models.DateField()
