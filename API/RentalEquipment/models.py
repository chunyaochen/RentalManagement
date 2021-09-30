from django.db import models

# Create your models here.
class Equiptment(models.Model):
    id =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    category = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serial_no = models.CharField(max_length=200)
def __str__(self):
    return str(self.__dict__)
class Meta:
        db_table = "Equipment"