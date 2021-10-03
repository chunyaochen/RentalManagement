from django.db import models
import datetime
BUY_RENT_CHOICES = (
    (True, 'BUY'),
    (False, 'RENT')
)

# Create your models here.
class Equiptment(models.Model):
    category = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serial_no = models.CharField(max_length=200)
def __str__(self):
    return str(self.__dict__)
class Meta:
        db_table = "Equipment"

class Vendor(models.Model):

    sales_person = models.CharField(max_length=200)
    address = models.CharField(max_length=200,default = "Here")
    email = models.EmailField(default="www.example.com")


class Rental(models.Model):

    equipment_id = models.ManyToManyField(Equiptment)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    receive_time = models.DateField()
    return_time = models.DateField()
    rental_rate = models.CharField(max_length=200,default="1")
    buy_rent = models.BooleanField(choices = BUY_RENT_CHOICES, default='RENT')
