
from django.urls import reverse

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории продуктов"




class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ {self.id} от {self.order_date} для {self.client.name}"

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])

