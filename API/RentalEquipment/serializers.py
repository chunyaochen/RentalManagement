from rest_framework import serializers 
from .models import Equiptment,Vendor,Rental
 
 
class EquipmentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Equiptment
        fields = (
            'id',
            'category',
            'make',
            'model',
            'serial_no')
class VendorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Vendor
        fields = (
            'id',
            'sales_person',
            'address',
            'email',
            )
class RentalSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Rental
        fields = (
            'id',
            'Equiptment',
            'Vendor',
            'recieve_time',
            'return_time',
            'rental_rate',
            'buy_rent')