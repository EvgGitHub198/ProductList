from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from .models import Products, Category
from .serializer import ProductsSerializer, CategorySerializer, AllCategoriesSerializer
from rest_framework import viewsets, permissions, generics


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AllCategoriesSerializer


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.prefetch_related('products').all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)