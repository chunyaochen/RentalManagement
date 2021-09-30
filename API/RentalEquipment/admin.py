from django.contrib import admin
from django.views.generic import ListView
from RentalEquipment.models import Equiptment


# Register your models here.
admin.site.register(Equiptment)
class Equiptment(ListView):
	model = Equiptment
