from django.db import models
from address.models import Address

class BillingProfile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"Billing Profile for {self.user.username}"