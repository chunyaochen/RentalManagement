from django.conf.urls import url 
from RentalEquipment import views
 
urlpatterns = [ 
    url(r'^api/Equipment$', views.eqipment_list),
    url(r'^api/Equipment/(?P<pk>[0-9]+)$', views.eqipment_detail),
    url(r'^api/Vendor$', views.vendor_list),
    url(r'^api/Vendor/(?P<pk>[0-9]+)$', views.vendor_detail),
    url(r'^api/Rental$', views.rental_list),
    url(r'^api/Rental/(?P<pk>[0-9]+)$', views.rental_detail),
]