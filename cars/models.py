from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=100, blank=False, null=False)
    brand = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    is_bought = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model}"
