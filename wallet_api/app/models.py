from datetime import date
from django.db import models

class Transaction(models.Model):
    date = models.DateField(default = date.today())
    category = models.CharField(max_length=100)
    memo = models.CharField(max_length=100)
    income = models.IntegerField(default=0)
    expenditure = models.IntegerField(default=0)
    def __str__(self):
        return str(self.date)
