from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField()
