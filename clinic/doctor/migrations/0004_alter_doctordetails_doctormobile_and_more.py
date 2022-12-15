# Generated by Django 4.1.2 on 2022-11-19 01:21

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_newpatient_patientmobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetails',
            name='doctormobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='newpatient',
            name='patientmobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
