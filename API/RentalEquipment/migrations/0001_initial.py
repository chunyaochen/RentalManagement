# Generated by Django 3.2.6 on 2021-10-05 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equiptment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('serial_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_person', models.CharField(max_length=200)),
                ('address', models.CharField(default='Here', max_length=200)),
                ('email', models.EmailField(default='www.example.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_time', models.DateField()),
                ('return_time', models.DateField()),
                ('rental_rate', models.CharField(default='1', max_length=200)),
                ('buy_rent', models.BooleanField(choices=[(True, 'BUY'), (False, 'RENT')], default='RENT')),
                ('equipment_id', models.ManyToManyField(to='RentalEquipment.Equiptment')),
                ('vendor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RentalEquipment.vendor')),
            ],
        ),
    ]
