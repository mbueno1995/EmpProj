from django.db import models

# Create your models here.
class Employee(models.Model):
    empno = models.IntegerField(unique=True)
    empname = models.CharField(max_length=200)
    password = models.CharField(max_length=20)



