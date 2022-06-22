from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Labor(models.Model):
    IS_ACTIVE = [('Y', 'Yes'),
                 ('N', 'No'), ]
    labor_class = models.CharField(max_length=100, blank=False)
    billing_code = models.CharField(max_length=20, blank=False)
    default_rates = models.IntegerField(blank=False)
    active = models.CharField(max_length=3, choices=IS_ACTIVE, default='Y')

    disasterLabor = models.Manager()


class Supply(models.Model):
    IS_ACTIVE = [('Y', 'Yes'),
                 ('N', 'No'), ]
    supply_code = models.CharField(max_length=100, blank=False)
    billing_code = models.CharField(max_length=20, blank=False)
    default_rates = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
