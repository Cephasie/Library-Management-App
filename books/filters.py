from django_filters import FilterSet
from .models import Book


class CustomFilter(FilterSet):
    model = Book
    fields = {
        'author_id':['exact'],
        'title': ['exact'],
        'copies': ['gt', 'lt']
    }
