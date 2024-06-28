from django.db import models

class Emp(models.Model):
    emp_name = models.CharField(max_length=255)
    emp_id = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length = 10)