from django.db import models

# Create your models here.
class Vehicle(models.Model):
    car_make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    plate_num = models.CharField(max_length=12, unique=True)
    price_day = models.DecimalField(max_digits=10, decimal_places=3)
    condition = models.CharField(max_length=8, blank=True, default='free')

    class Meta:
        db_table = 'vehicles'

    
    REQUIRED_FIELDS = ['car_make', 'model', 'plate_num', 'price_day']

    
    def create(self, **kwargs):
        record = self.model(**kwargs)
        record.save()
        return record
        