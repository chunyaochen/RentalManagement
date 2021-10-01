from django.shortcuts import render

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from RentalEquipment.models import Equiptment
from RentalEquipment.serializers import EquipmentSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def eqipment_list(request):
    if request.method == 'GET':
        eqipments = Equiptment.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            eqipments = eqipments.filter(title__icontains=title)
        eqipments_serializer = EquipmentSerializer(eqipments, many=True)
        return JsonResponse(eqipments_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        eqipment_data = JSONParser().parse(request)
        eqipments_serializer = EquipmentSerializer(data=eqipment_data)
        if eqipments_serializer.is_valid():
            eqipments_serializer.save()
            return JsonResponse(eqipments_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(eqipments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Equiptment.objects.all().delete()
        return JsonResponse({'message': 'Delete all,{} eqipments were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def eqipment_detail(request, pk):
    try: 
        eqipment = Equiptment.objects.get(pk=pk) 
    except Equiptment.DoesNotExist: 
        return JsonResponse({'message': 'The equiptment does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        eqipments_serializer = EquipmentSerializer(eqipment) 
        return JsonResponse(eqipments_serializer.data) 
 
    elif request.method == 'PUT': 
        eqipment_data = JSONParser().parse(request) 
        eqipments_serializer = EquipmentSerializer(eqipment, data=eqipment_data) 
        if eqipments_serializer.is_valid(): 
            eqipments_serializer.save() 
            return JsonResponse(eqipments_serializer.data) 
        return JsonResponse(eqipments_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        eqipment.delete() 
        return JsonResponse({'message': 'The equiptment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

