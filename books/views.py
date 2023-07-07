
from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated, IsAuthenticatedOrReadOnly 
from .permissins import IsOwnerOrReadOnly

# Create your views here.

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[IsAuthenticatedOrReadOnly ]

# RetrieveAPIView RetrieveUpdateAPIView
class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[IsOwnerOrReadOnly]
