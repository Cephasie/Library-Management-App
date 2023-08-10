from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author


# Create your views here.

# def welcome(request):
#     query_set = Author.objects.all()
#     return render(request, "books/welcome.html", {"author": list(query_set)})
#
#
# users = [
#     {"name": "Ayodeji"},
#     {"name": "Cephas"},
#     {"name": "Asa"}
# ]
#
#
# def welcome(request):
#     return render(request, 'books/welcome.html', {"students": users})
#
#
def greet(request):
    return HttpResponse("Good morning Oga oh!!!")


@api_view()
def book_list(request):
    return Response('ok')


def book_detail(request, pk):
    return Response(pk)