# Generated by Django 2.0.5 on 2018-07-04 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolarDB', '0022_auto_20180620_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaseproperty',
            name='totalContractPrice',
            field=models.FloatField(default=None),
        ),
    ]
