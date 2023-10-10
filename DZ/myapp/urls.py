from django.urls import path
from . import views
urlpatterns = [
    # URL-маршруты для клиентов
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client-delete'),

    # URL-маршруты для товаров
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),

    # URL-маршруты для заказов
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order_update'),
]
