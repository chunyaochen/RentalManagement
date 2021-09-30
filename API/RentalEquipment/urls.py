from django.conf.urls import url 
from RentalEquipment import views 
 
urlpatterns = [ 
    url(r'^api/Equipment$', views.eqipment_list),
    url(r'^api/Equipment/(?P<pk>[0-9]+)$', views.eqipment_detail),
    url(r'^api/Equipment/published$', views.eqipment_list_published)
]