from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    """
    Users Django's User model but re-defines the required username field to
    be the email field instead. Username still available via Profile reference.
    """
    username = None
    email = models.EmailField(unique=True)

    # instantiate the custom user manager
    objects = CustomUserManager()

    # required from base
    is_active = models.BooleanField(name='active', default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # profile in which the majority of user data is stored. Not required
    profile = models.OneToOneField(
        to="UserProfile",
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_DEFAULT  # set reference to NULL but keep user
    )

class UserProfile(models.Model):
    """
    reference for User data
    """
    user = models.OneToOneField(
        to=CustomUser,
        on_delete=models.CASCADE
    )

    # defines fields which can be associated with a single user
    first_name = models.TextField(max_length=256, blank=True, null=True)
    last_name = models.TextField(max_length=256, blank=True, null=True)
