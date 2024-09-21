"""
URL configuration for customers_orders_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers.views import CustomerViewSet
from orders.views import OrderViewSet


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('oidc/', include('oidc_provider.urls', namespace='oidc_provider')),
    path('api/', include('orders.urls')),  # Include the orders URLs
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    
]


