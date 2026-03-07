from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model representing a user profile.

    Extends the built-in :model:`auth.User` via a one-to-one relationship
    to store additional user information such as a favourite city.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the associated username as a string."""
        return self.user.username
