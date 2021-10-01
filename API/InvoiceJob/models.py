from django.db import models
import datetime
from RentalEquipment.models import Rental


class Job(models.Model):
    """
    Represents a construction job , one-to-one with Invoice,
    eventually  a job has many rentals
    """
    #invoice = models.OneToOneField(Invoice , on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200,default="name")
    needed_from = models.DateField()
    needed_to = models.DateField()
    rentals = models.ManyToManyField(Rental)

# Create your models here.

class Invoice(models.Model):
    """
    Represents an invoice for a Job
    which includes totals , and date
    """
    job = models.OneToOneField(Job, on_delete=models.CASCADE, null=True)
    invoice_date = models.DateField(default=datetime.date.today)
    rental_period = models.IntegerField()
    invoice_amount = models.IntegerField()
    


