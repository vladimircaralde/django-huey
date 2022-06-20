from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    fuel_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name