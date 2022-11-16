from rest_framework import routers

from django.urls import path, include
from .views import BookViewSet
# from .views import  BookAPIMixins, BooksAPIMixins
# from .views import HelloAPI, BookAPI, BooksAPI,


# urlpatterns = [
       
#     path('hello/', HelloAPI.as_view()),
#     path('cbv/books/',BooksAPI.as_view()),
#     path('cbv/book/<int:bid>/', BookAPI.as_view()),
#     path('mixin/books/', BooksAPIMixins.as_view()),
#     path('mixin/book/<int:bid>/', BookAPIMixins.as_view())
# ]

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls

