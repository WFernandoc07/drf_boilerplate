# Generated by Django 4.2.7 on 2023-11-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='plate_num',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
