from django.shortcuts import render

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from RentalEquipment.models import Equiptment,Vendor,Rental
from RentalEquipment.serializers import EquipmentSerializer,VendorSerializer,RentalSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.response import Response


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

@api_view(['GET', 'POST', 'DELETE'])
def vendor_list(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            vendors = vendors.filter(title__icontains=title)
        Vendor_serializer = VendorSerializer(vendors, many=True)
        return JsonResponse(Vendor_serializer.data, safe=False)
 
    elif request.method == 'POST':
        vendor_data = JSONParser().parse(request)
        vendor_serializer = VendorSerializer(data=vendor_data)
        if vendor_serializer.is_valid():
            vendor_serializer.save()
            return JsonResponse(vendor_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(vendor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Vendor.objects.all().delete()
        return JsonResponse({'message': 'Delete all,{} eqipments were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail(request, pk):
    try: 
        vendor = Vendor.objects.get(pk=pk) 
    except Vendor.DoesNotExist: 
        return JsonResponse({'message': 'The vendor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        vendor_serializer = VendorSerializer(vendor) 
        return JsonResponse(vendor_serializer.data) 
 
    elif request.method == 'PUT': 
        vendor_data = JSONParser().parse(request) 
        vendor_serializer = VendorSerializer(vendor, data=vendor_data) 
        if vendor_serializer.is_valid(): 
            vendor_serializer.save() 
            return JsonResponse(vendor_serializer.data) 
        return JsonResponse(vendor_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        vendor.delete() 
        return JsonResponse({'message': 'The vendor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#@authentication_classes([ BasicAuthentication])
@api_view(['GET', 'POST', 'DELETE'])
def rental_list(request):
    if request.method == 'GET':


        rentals = Rental.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            rentals = rentals.filter(title__icontains=title)
        Rental_serializer = RentalSerializer(rentals, many=True)
        return JsonResponse(Rental_serializer.data, safe=False)

    elif request.method == 'POST':
        rental_data = JSONParser().parse(request)
        rental_serializer = RentalSerializer(data=rental_data)
        if rental_serializer.is_valid():
            rental_serializer.save()
            return JsonResponse(rental_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(rental_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Rental.objects.all().delete()
        return JsonResponse({'message': 'Delete all,{} rental record were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def rental_detail(request, pk):
    try: 
        rental = Rental.objects.get(pk=pk) 
    except Rental.DoesNotExist: 
        return JsonResponse({'message': 'The rental record does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        rental_serializer = RentalSerializer(rental) 
        return JsonResponse(rental_serializer.data) 
 
    elif request.method == 'PUT': 
        rental_data = JSONParser().parse(request) 
        rental_serializer = RentalSerializer(rental, data=rental_data) 
        if rental_serializer.is_valid(): 
            rental_serializer.save() 
            return JsonResponse(rental_serializer.data) 
        return JsonResponse(rental_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        rental.delete() 
        return JsonResponse({'message': 'The rental record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)