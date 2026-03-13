from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Model representing a physical address.

    Related to :class:`lettings.models.Letting` via a one-to-one relationship.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Return the street number and street name as a string."""
        return f'{self.number} {self.street}'

    class Meta:
        """Set the plural name for the Address model in the admin interface."""
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """Model representing a property letting.

    Related to :class:`lettings.models.Address` via a one-to-one relationship.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the letting title as a string."""
        return self.title
