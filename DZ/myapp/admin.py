from django.contrib import admin
from .models import Product, Order, Client, Category

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Category)