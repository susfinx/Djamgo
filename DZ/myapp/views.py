from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Order

def order_list(request):

    last_week_orders = Order.objects.filter(
        date_ordered__gte=timezone.now() - timezone.timedelta(days=7)
    )

    last_month_orders = Order.objects.filter(
        date_ordered__gte=timezone.now() - timezone.timedelta(days=30)
    )

    last_year_orders = Order.objects.filter(
        date_ordered__gte=timezone.now() - timezone.timedelta(days=365)
    )

    context = {
        'last_week_orders': last_week_orders,
        'last_month_orders': last_month_orders,
        'last_year_orders': last_year_orders,
    }

    return render(request, 'order_list.html', context)


class ClientListView(ListView):
    model = Client
    template_name = 'myapp/client_list.html'  # Указывает путь к шаблону
    context_object_name = 'clients'  # Указывает имя переменной контекста, содержащей список клиентов

class ClientDetailView(DetailView):
    model = Client

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

class ClientDeleteView(DeleteView):
    model = Client
    success_url = '/clients/'

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/'

class OrderListView(ListView):
    model = Order

class OrderDetailView(DetailView):
    model = Order

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/orders/'
