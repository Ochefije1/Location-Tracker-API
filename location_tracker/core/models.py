from django.db import models

class PhoneNumberLocation(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    map_url = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = "Phone Number Locations"
