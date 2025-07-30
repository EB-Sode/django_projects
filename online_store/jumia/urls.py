from django.urls import path, include
from .views import ProductListCreateAPIView, ProductViewSet
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'products', ProductViewSet)  # This handles full CRUD via /products/

urlpatterns = [
    path('products-lite/', ProductListCreateAPIView.as_view(), name='product-lite'),  # Limited list/create
    path('', include(router.urls)),  # Includes all ViewSet routes
    path("api/products", views.ProductListCreateAPIView.as_view(), name="product_list_create"),
]
