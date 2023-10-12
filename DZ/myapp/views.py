from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm
from django.shortcuts import render
from django.utils import timezone
from .models import Order
from django.core.files.storage import FileSystemStorage


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


def client_form(request):
    message = ''

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            client = Client(name=name, email=email, phone_number=phone_number, address=address)
            client.save()
            message = 'Пользователь сохранен'
        else:
            message = 'Ошибка в данных'
    else:
        form = ClientForm()

    return render(request, 'myapp/client_form.html', {'form': form, 'message': message})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image,)
            product=Product(name=name,description=description,price=price,quantity=quantity,)
            product.save()
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})



class ClientListView(ListView):
    model = Client
    template_name = 'myapp/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client

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





