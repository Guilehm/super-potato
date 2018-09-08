from django.db import models


class Patient(models.Model):
    registration = models.CharField(max_length=11)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=200, null=True, blank=True)
    birth_date = models.DateField()
    doc = models.CharField(max_length=20)
    home_phone_number = models.CharField(max_length=20, null=True, blank=True)
    cell_phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
