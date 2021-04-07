from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.show_all_products),
    path('products/<int:product_id>', views.get_one_product),
    path('categories/', views.show_all_categories),
    path('categories/<int:category_id>', views.get_one_category),
    path('categories/<int:category_id>/products', views.get_products_by_category)
]