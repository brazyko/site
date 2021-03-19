from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import *
from cart.models import Order
from parts.models import Product
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer