# Django imports for app configuration and internationalization
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserAuthConfig(AppConfig):
    """
    Configuration class for the User Authentication application.
    
    This app handles all user authentication related functionality including:
    - User registration and login
    - OTP verification
    - Account locking mechanism
    - Email notifications
    
    Attributes:
        default_auto_field (str): Specifies the primary key type for models
        name (str): The Python package name of the app
        verbose_name (str): Human-readable name of the app (translatable)
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.user_auth'
    verbose_name = _("User Auth")
