from django.db import models
class Person(models.Model):
    name = models.CharField(max_length = 50)
    number = models.IntegerField()
    address = models.CharField(max_length = 100)
    
    