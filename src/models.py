from django.db import models

# Create your models here.
class Car(models.Model):

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    email = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

