from api.src.authentication.models import User
from django.db import models

# Create your models here.
class Cocktails(models.Model):
    name = models.CharField(max_length=80, unique=False, blank=False)
    price = models.DecimalField(max_digits=12, unique=False, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
