from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework import permissions
from .serializers import JobSerializer, InvoiceSerializer
from .models import Job, Invoice



#___________________________________ Invoice ________________________________
# Class based api views

class InvoiceViewset(viewsets.ModelViewSet):
    """
    API Endpoint that allows invoices to be viewed
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    # permissions to be added at a later point
    #permission_classes = [permissions.IsAuthenticated]

# Create your views here.
# try generic apidetail
class InvoiceDetail( mixins.RetrieveModelMixin,
                      generics.GenericAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)



class InvoiceCreate( mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
    Generic APIView for creating an Invoice
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def post(self,request, *args,**kwargs):
        return self.create(request, *args, **kwargs)


class InvoiceUpdate( mixins.UpdateModelMixin,
                      generics.GenericAPIView):
    """
    Generic APIView for updating an Invoice
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def put(self,request, *args,**kwargs):
        return self.update(request, *args, **kwargs)


class InvoiceDelete(mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    """
    generic APIView for deleting Invoice
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def delete(self, request, *args,**kwargs):
        return self.destroy(request,*args,**kwargs)


#___________________________________ Job ________________________________
# Class based api views


class JobViewset(viewsets.ModelViewSet):
    """
    API Endpoint that allows jobs to be viewed
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # permissions to be added at a later point
    #permission_classes = [permissions.IsAuthenticated]


# Create your views here.
# try generic apidetail
class JobDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # requires authentication
    permission_classes =  [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class JobCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    """
    Generic APIView for creating an JOb
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class JobUpdate(mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    """
    Generic APIView for updating an Invoice
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class JobDelete(mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    generic APIView for deleting Job
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

