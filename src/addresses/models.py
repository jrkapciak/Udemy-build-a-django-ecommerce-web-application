from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing','Billing'),
    ('shipping', 'Billing')
)

class Address(models.Model):
    billing_profil = models.ForeignKey(BillingProfile)
    address_type = models.CharField(max_length=120)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profil)
