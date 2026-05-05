from django.urls import include, path
from .views import BookListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookListView, basename='book')




urlpatterns = [
    # path('books/', views.book_list, name='book-list'), #function based view
    # path('books/', BookListView.as_view(), name='book-list'), #class based view
    path('', include(router.urls)), #viewsets
]