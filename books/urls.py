from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from . import views

router = SimpleRouter()
# router.register('books', views.BookViewSet)
# router.register('authors', views.AuthorViewSet)
# router.register('reviews', views.ReviewViewSet)
# print(router.urls)

# books_router = routers.NestedDefaultRouter(router, 'books', lookup='books')
# books_router.register('reviews', views.ReviewViewSet, basename='book-reviews')

# urlpatterns = router.urls + books_router.urls
urlpatterns = router.urls

# urlpatterns = [
# path('book/', views.book_list),
# path('book/', views.BookViewSet.as_view()),
# path('book/<int:pk>', views.BookDetail.as_view()),
# path('', include(router.urls)),

# path('author/', views.AuthorList.as_view()),
# path('author/<int:pk>', views.AuthorDetail.as_view(), name="author-detail")
# path('welcome/', views.welcome),
# path('hello/', views.hello),
# path('books/pk/', views.get_books)
# ]
