from rest_framework import serializers

from .models import Category, Restoran, Product, TableProducts, Table


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'restoran', )

class RestoranSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        restoran = Restoran(name=validated_data['name'], image=validated_data['image'], tables=validated_data['tables'])
        restoran.save()
        for i in range(0,restoran.tables):
            t = Table(number=i+1, restoran=restoran, color=1)
            t.save()
        return restoran
        
    class Meta:
        model = Restoran
        fields = ('id', 'name', 'image', 'tables', )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'body', 'status', 'unit', 'price', 'image', 'category', )

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'body', 'status', 'unit', 'price', 'image', )

class TableProductsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        restoran = Restoran.objects.filter(id=validated_data['product'].category.restoran.id).first()
        if validated_data['table']<=restoran.tables:
            a = TableProducts(table=validated_data['table'], product=validated_data['product'], unit=validated_data['unit'], status=validated_data['status'])
            a.save()
            return a
        msg = "This is restoran not table"
        raise exceptions.ValidationError(msg)

    class Meta:
        model = TableProducts
        fields = ('id', 'table', 'product', 'unit', 'status')

class TableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'number', 'restoran', 'color')