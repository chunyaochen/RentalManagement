from rest_framework import serializers 
from .models import Equiptment
 
 
class EquipmentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Equiptment
        fields = (
            'id',
            'category',
            'make',
            'model',
            'serial_no')