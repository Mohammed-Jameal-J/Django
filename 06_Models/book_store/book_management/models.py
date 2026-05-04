from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"

class AuthorProfile(models.Model):
    bio = models.TextField(blank=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', default=1)
    categories = models.ManyToManyField(Category, related_name='books')
    def __str__(self):
        return f"{self.id} - {self.title}"