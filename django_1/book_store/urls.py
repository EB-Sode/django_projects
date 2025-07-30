from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import path, include
from .views import SignUpView  # make sure you have this view defined

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_product, name="create_product"),
    path("create-many/", views.products_add_many, name="products_add_many"),
    path('delete-all/', views.delete_all_products, name='delete_all_products'),
    path("update-product/", views.update_product, name="update_product"),
    path("view-products/", views.view_all_product, name="view_all_products"),
    path("products-by-price/", views.products_by_price, name="products_by_price"),
    path("select-category/", views.select_category, name="select_category"),
    # Book-related URLs
    path("add-book/", views.add_book, name="add_book"),
    path("view-books/", views.view_books, name="view_all_books"),
    path("delete-all-books/", views.delete_all_books, name="delete_all_books"),
    path("add-many-books/", views.books_add_many, name="books_add_many"),

    path('accounts/', include('django.contrib.auth.urls')),
    
    # Profile page after login
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),

    # Signup route
    path('signup/', SignUpView.as_view(), name='signup'),
]