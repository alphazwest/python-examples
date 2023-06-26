from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom Manager class for the custom User modeling.
    """
    def create_user(self, email: str, password: str, **fields):
        """
        Creates a user given the email and password.
        """
        if not email:
            raise ValueError("User must have valid email!")

        # set the appropriate fields, save, return newly-created model
        email = self.normalize_email(email=email)
        user = self.model(email=email, **fields)
        user.set_password(raw_password=password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **fields):
        """
        Creates a new instance of a superuser-enabled User object.
        """
        # set proper permissions flags and assume active
        fields.setdefault('is_staff', True)
        fields.setdefault('is_superuser', True)
        fields.setdefault('is_active', True)

        # validation checks
        if not fields.get('is_staff'):
            raise ValueError("Super must set is_staff=True")
        if not fields.get('is_superuser'):
            raise ValueError("Superuser must set is_superuser=True")
        return self.create_user(email=email, password=password, **fields)

