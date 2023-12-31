# # class Field:
# #     model = Author
# #     fields = ['first_name', 'last_name', 'email']
# #
# #
# # class BookSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Book
# #         fields = ['id', 'title', 'isbn', 'genre', 'copies']
# #
# #         author = serializers.HyperlinkedRelatedField(
# #             Author.objects.all(),
# #             view_name="author-detail"
# #         )
#
#
# from rest_framework import serializers
# from .models import Book, Author, Reviews
#
#
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['first_name', 'last_name', 'email']
#
#
# class BooKSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'isbn', 'genre', 'copies', 'author', 'date_published']
#
#     # name_of_book =serializers.CharField(source='title')
#
#     author = serializers.HyperlinkedRelatedField(
#         queryset=Author.objects.all(),
#         view_name="author-detail"
#     )
#
#
# class CreateAuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['first_name', 'last_name', 'email']
#
#
# class CreateBooKSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['title', 'isbn', 'genre', 'copies', 'author']
#
#
# class ReviewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reviews
#         fields = ['id', 'name', 'description', 'book']
#
#     # name_of_book =serializers.CharField(source='title')
#
# # class BookSerializer (serializers.Serializer):
# #     title = serializers.CharField(max_length=200)
# #     isbn = serializers.CharField(max_length=13)
# #     genre = serializers.CharField(max_length=8)
#
#
# # class AuthorSerializer(serializers.Serializer):
# #     first_name = serializers.CharField(max_length=150)
# #     last_name = serializers.CharField(max_length=150)
# #     email = serializers.EmailField
