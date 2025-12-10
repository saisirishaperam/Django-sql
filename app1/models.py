from django.db import models

# Create your models here.
class student(models.Model):
    std_name = models.CharField(max_length=50)
    std_pin = models.IntegerField()
    