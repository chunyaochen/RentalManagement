from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()
#router.register(r'invoices', InvoiceViewset)
router.register(r'jobs', JobViewset)
router.register(r'invoices', InvoiceViewset)
# patterns for create , read detail, update , delete on job & invoice (single)
urlpatterns = [
    path('', include(router.urls)),
    path('job/create/', JobCreate.as_view() ),
    path('job/<int:pk>/', JobDetail.as_view()),
    path('job/update/<int:pk>/', JobUpdate.as_view()),
    path('job/delete/<int:pk>/', JobDelete.as_view()),
    path('invoice/create/', InvoiceCreate.as_view()),
    path('invoice/<int:pk>/', InvoiceDetail.as_view()),
    path('invoice/update/<int:pk>/', InvoiceUpdate.as_view()),
    path('invoice/delete/<int:pk>/', InvoiceDelete.as_view()),
]