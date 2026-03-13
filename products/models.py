from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField(max_length=255)
    discount = models.FloatField()