from django.db import models

from admins.models import Admin

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    quantite=models.IntegerField()
    price=models.FloatField()
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
