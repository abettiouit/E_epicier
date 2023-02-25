from django.db import models
from admins.models import Admin

from products.models import Product
from clients.models import Client

# Create your models here.
class Credit(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    quantite=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()
    etat=models.BooleanField(default=False)