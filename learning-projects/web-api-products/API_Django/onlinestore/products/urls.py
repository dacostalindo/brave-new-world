from django.urls import path
from .views import product_detail, product_list #ProductDetailView, ProductListView

urlpatterns = [ 
    path("products/", product_list, name="product-list"),
    path("product/<int:pk>/", product_detail, name="product-detail"),
]