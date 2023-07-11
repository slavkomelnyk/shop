from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=30)
    text = models.TextField()
    big_text = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='static/image')

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
