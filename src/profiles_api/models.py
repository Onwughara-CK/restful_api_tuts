from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class UserProfileManager(BaseUserManager):
    """
    use to manage UserProfile
    """

    def create_user(self, email, name, password=None):
        """
        use to create user
        """

        if not email:
            raise ValueError("Please provide a valid email")
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        use to create super user
        """

        user = self.create_user(name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Use to create our custom model
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDs = ['name']

    objects = UserProfileManager()

    def get_full_name(self):
        """
        Use to get user's full name
        """

        return self.name

    def get_short_name(self):
        """
        use to get users short name
        """

        return self.name[0:2]

    def __str__(self):
        """
        use to convert object to string
        """

        return self.email
