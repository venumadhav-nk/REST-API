from django.db import models


# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length=20)
    salary = models.IntegerField()
    role = models.CharField(max_length=20)
    mobile = models.BigIntegerField()

    def __str__(self) :
        return self.name