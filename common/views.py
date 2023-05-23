from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser

from .models import Category
from common.serializers import CategorySerializer


# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

