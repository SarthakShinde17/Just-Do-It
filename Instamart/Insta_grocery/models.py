from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=2)
    image = models.ImageField(upload_to='images/',null=True, blank=True)


def __str__(self):
        return self.name