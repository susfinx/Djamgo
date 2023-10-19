from random import choice, randint, uniform
from django.core.management.base import BaseCommand
from myapp.models import Category, Product

class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of products to generate')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')

        for i in range(1, count + 1):
            products.append(Product(
                name=f'Product {i}',
                category=choice(categories),
                description='Long product description that nobody reads',
                price=uniform(0.01, 999_999.99),
                quantity=randint(1, 10_000),
            ))

        Product.objects.bulk_create(products)
