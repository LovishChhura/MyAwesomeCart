# Generated by Django 4.0.2 on 2022-03-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_oder_id_orderupdate_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
