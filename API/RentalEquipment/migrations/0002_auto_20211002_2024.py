# Generated by Django 3.2.6 on 2021-10-03 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalEquipment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='Equiptment',
            new_name='equipment_id',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='Vendor',
            new_name='vendor_id',
        ),
    ]
