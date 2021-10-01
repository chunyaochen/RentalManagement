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

    Equiptment = models.ManyToManyField(Equiptment)
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    recieve_time = models.DateTimeField(default=datetime.datetime.now)
    return_time = models.DateTimeField(default=datetime.datetime.now)
    rental_rate = models.CharField(max_length=200,default="1")
    buy_rent = models.BooleanField(choices = BUY_RENT_CHOICES, default='RENT')