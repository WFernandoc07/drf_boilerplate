from django.db import models
from users.models import User
from vehicles.models import Vehicle

# Create your models here.
class Rent(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    total_pay = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.RESTRICT)
    
    class Meta:
        db_table = 'rents'

    REQUIRED_FIELDS = ['date_start', 'date_end', 'user', 'vehicle']

    def create(self, **kwargs):
        record = self.model(**kwargs)
        record.save()
        return record
        