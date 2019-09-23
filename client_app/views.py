from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Category, Product, Restoran, TableProducts, Table
from .serializers import CategorySerializer, RestoranSerializer, ProductListSerializer, ProductSerializer, TableProductsSerializer, TableListSerializer
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class RestoransViewSet(viewsets.ModelViewSet):
    queryset = Restoran.objects.all()
    serializer_class = RestoranSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class RestoranTablesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        r_id = self.kwargs['restoran_id']
        return Category.objects.filter(restoran__id=r_id)

class ProductListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        c_id = self.kwargs['c_id']
        return Product.objects.filter(category__id=c_id)

class ProductDetailViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        p_id = self.kwargs['p_id']
        return Product.objects.filter(id=p_id)

class TableProductsAddViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = TableProductsSerializer
    def get_queryset(self):
        r_id = self.kwargs['restoran_id']
        t = self.kwargs['table_number']
        a = Table.objects.filter(number=t, restoran__id=r_id).first()
        return TableProducts.objects.filter(table=a)
    # authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]
    

class TableProductsListsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TableProductsSerializer
    def get_queryset(self):
        r_id = self.kwargs['r_id']
        t_id = self.kwargs['t_id']
        return TableProducts.objects.filter(restoran_id=r_id,table=t_id)

class TableListViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableListSerializer
