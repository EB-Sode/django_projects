from django.shortcuts import render
from .models import Product, Book
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
'''This code is for a Django application that manages a book store. 
It includes views for creating, deleting, updating, and viewing products (books) in the store. 
The models define the structure of the data, and the views handle HTTP requests to perform operations on the data.
'''


def index(request): return HttpResponse("Welcome to my book store.")

#create products
def create_product(request):
    new_product = Product(name="Dettol", description="Bathing antiseptic soap", price="20.56", category= "Toiletry")
    new_product.save()
    return HttpResponse("Product created successfully.")

#delete all products
def delete_all_products(request):
    delete_product = Product.objects.all().delete()
    return HttpResponse("All products deleted successfully.")

#update products
def update_product(request):
    update_product = Product.objects.update(
        name= "Dettol", description ="Bathing antiseptic soap",
        defaults= {"price": "22.10", "category":"hygiene"}
    )
    return HttpResponse("Product updated successfully.")

#view all products
def view_all_product(request):
    products = Product.objects.all()

#select product by price
def products_by_price(request):
    products_by_price= Product.objects.order_by('price')

#filter products by category
def select_category(request):
    products_by_category = Product.objects.filter(category='Toiletry')

#create_many
many_products = [
    Product(name="Insecticide", description= "mosquito repelant", price= "300.99", category= "groceries"),
    Product(name= "Tissue paper", description= "Soft and strong", price="15.23", category="groceries")
]
def products_add_many(request):
    products_add_many = Product.objects.bulk_create(many_products)
    return HttpResponse("Many products added successfully.")


'''This code is for a Django application that manages a book store. 
It includes views for creating, deleting, updating, and viewing products (books) in the store. 
The models define the structure of the data, and the views handle HTTP requests to perform operations on the data.
'''
#create products
def add_book(request):
    new_book = Book(title="Dead man's chest", author="Robert Louis Stevenson", date_published="1883-04-15")
    new_book.save()
    return HttpResponse("Book created successfully.")

def delete_all_books(request):
    delete_all_books= Book.objects.all().delete()
    return HttpResponse("Deleted all books")

def view_books(request):
    view_books = Book.objects.all()
    return HttpResponse("All books displayed")

many_books = [
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", date_published="1925-04-10"),
    Book(title="1984", author="George Orwell", date_published="1949-06-08"),
    Book(title="To Kill a Mockingbird", author="Harper Lee", date_published="1960-07-11")
]
def books_add_many(request):
    books_add_many = Book.objects.bulk_create(many_books)
    return HttpResponse("Many books added successfully.")

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"