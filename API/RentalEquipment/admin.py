from django.contrib import admin
from django.views.generic import ListView
from RentalEquipment.models import Equiptment,Rental,Vendor


# Register your models here.
admin.site.register(Equiptment)
class Equiptment(ListView):
	model = Equiptment
admin.site.register(Rental)
class Equiptment(ListView):
	model = Equiptment
admin.site.register(Vendor)
class Equiptment(ListView):
	model = Equiptment
