from minhascontas.authentication.models import User
from django.db import models
from django.utils import timezone


class Bill(models.Model):
    TYPES = (
        ('E', 'ENTRADA'),
        ('S', 'SAIDA'),
        )
    name = models.CharField(max_length=150)
    type_bill = models.CharField(max_length=1, choices=TYPES)
    value = models.FloatField()
    date = models.DateField(default=timezone.now)
    is_recourrent = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name