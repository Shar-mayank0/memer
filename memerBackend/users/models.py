from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # """
    # CustomUser

    # This class inherits from Django’s AbstractUser, which provides the following fields and functionality:

    # Fields:
    #     username (CharField):
    #         • Unique identifier for the user.
    #         • Required by default (can be customized with a unique email instead).

    #     first_name (CharField):
    #         • Stores the user’s given name.
    #         • Optional by default, can be required if needed.

    #     last_name (CharField):
    #         • Stores the user’s family name.
    #         • Optional by default, can be required if needed.

    #     email (EmailField):
    #         • Stores the user’s email address.
    #         • Optional by default, can be made unique if desired.

    #     password (CharField):
    #         • Stores a hashed representation of the user’s password.
    #         • Managed by Django’s authentication system; do not handle directly.

    #     groups (ManyToManyField to Group):
    #         • Associates the user with one or more groups.
    #         • Useful for managing permissions collectively.

    #     user_permissions (ManyToManyField to Permission):
    #         • Assigns specific permissions to the user (distinct from group permissions).
    #         • Used by Django’s authorization system.

    #     is_staff (BooleanField):
    #         • Designates whether the user can access the Django admin interface.
    #         • Must be True for users to log into the admin site.

    #     is_active (BooleanField):
    #         • Indicates whether this user’s account is considered active.
    #         • Uncheck this instead of deleting accounts for safe deactivation.

    #     is_superuser (BooleanField):
    #         • Grants all permissions to the user without explicitly assigning them.
    #         • Overridden checks for staff status and user permissions.

    #     last_login (DateTimeField):
    #         • Records the date and time of the user’s most recent login.
    #         • Automatically updated by Django’s authentication system.

    #     date_joined (DateTimeField):
    #         • Stores the date and time the user was created.
    #         • Typically set automatically to the time of user registration.

    # Methods and Behavior:
    #     • Django’s authentication backend and built-in functions (e.g., set_password, check_password) are available.
    #     • Permission checks rely on group membership, specific user permissions, or superuser status.

    # Summary:
    #     CustomUser extends the core user functionality provided by Django’s AbstractUser. 
    #     By inheriting AbstractUser, you gain built-in fields and authentication 
    #     mechanisms, as well as permission management and utility methods for user handling.
    # """
    pass
