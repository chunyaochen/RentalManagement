from rest_framework import viewsets, mixins, generics
from rest_framework import status
from rest_framework import viewsets, mixins, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job, Invoice
from .serializers import JobSerializer, InvoiceSerializer
from core.models import CustomUser


class ExampleView(APIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        usr_str = ''
        if request.user.is_authenticated:
            content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.user.isAdmin)
            }
        else:
            content = {
                'user': 'Anonymous',  # `django.contrib.auth.User` instance.
                'auth': 'None'
            }
        return Response(content,status.HTTP_200_OK)






@api_view(['POST'])
def auth_request(request):
    """
    view used by Angular AuthService,
    always returns 200,
    but it also returns an authcode
    1 = User,
    2 = Admin,
    3 = No User with User/Password found
    """
    if request.method == 'POST':
        user = request.user
        is_valid = checkLoginStatus(user)
        # check if not valid user
        if is_valid == False:
            return Response("{authcode:3}", status.HTTP_200_OK);
        #check if valid user
        if is_valid == True:
            #check if user is admin
            if request.user.isAdmin == True:
                return Response("{authcode:2", status.HTTP_200_OK);
            return Response("{authcode:1}", status.HTTP_200_OK);

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
    #permission_class = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        # return unauthorized if not authenticated

        #if request.user.isAdmin == True:
        return self.retrieve(request, *args, **kwargs)

        #return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)



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
    #permission_classes =  [permissions.IsAuthenticated]
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

