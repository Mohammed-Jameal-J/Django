from rest_framework import serializers
from .models import Book, Author, AuthorProfile, Category

class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = ['bio']

class AuthorSerializer(serializers.ModelSerializer):
    profile = AuthorProfileSerializer()

    class Meta:
        model = Author
        fields = ['id', 'name', 'profile']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    categories = CategorySerializer(many=True)

    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True , source='author')
    category_ids = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='categories', many=True, write_only=True , source='categories')

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'categories', 'author_id', 'category_ids']

