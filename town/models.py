from django.db import models
from django.utils.timezone import now


class Town(models.Model):
    id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(default=now, editable=False)
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    average_age = models.DecimalField(max_digits=5, decimal_places=2)
    district_code = models.IntegerField()
    department_code = models.IntegerField()
    region_code = models.IntegerField()
    region_name = models.CharField(max_length=100)
