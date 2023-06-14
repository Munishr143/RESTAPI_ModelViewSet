from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrudActions(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductMS
