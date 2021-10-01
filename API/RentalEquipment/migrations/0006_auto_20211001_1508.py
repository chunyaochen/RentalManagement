# Generated by Django 3.2.7 on 2021-10-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentalEquipment', '0005_auto_20211001_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='rental_rate',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.CharField(default='Here', max_length=200),
        ),
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.EmailField(default='www.example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='rental',
            name='buy_rent',
            field=models.BooleanField(choices=[(True, 'BUY'), (False, 'RENT')], default='RENT'),
        ),
    ]