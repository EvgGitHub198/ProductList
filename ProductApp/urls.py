from rest_framework import routers
from .api import ProductsViewSet, CategoriesViewSet, category_list
from django.urls import path, include


router = routers.DefaultRouter()
router.register('api/products', ProductsViewSet, 'products')
router.register('api/categories', CategoriesViewSet, 'categories')

urlpatterns = [
    path('categories_of_products/', category_list, name='category-list'),

]

urlpatterns += router.urls