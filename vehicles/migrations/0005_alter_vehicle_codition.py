# Generated by Django 4.2.7 on 2023-11-22 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_alter_vehicle_codition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='codition',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
