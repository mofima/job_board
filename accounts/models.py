from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.utils.translation import gettext_lazy as _  


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **otherfields):
        if not email:
            raise ValueError('users must have email address')
        email = self.normalize_email(email=email, **otherfields)
        user = self.model(email=email, **otherfields)
        user.set_password(password)
        user.save()
        return user 
    
    def create_superuser(self, email, password=None, **otherfields):
        otherfields.setdefault('is_staff', True)
        otherfields.setdefault('is_active', True)
        otherfields.setdefault('is_superuser', True)

        if otherfields.get('is_staff') is not True:
            raise ValueError('is_staff must be set to true')
        if otherfields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be set to true')
        
        return self.create_user(email, password, **otherfields)
    

class CustomUser(AbstractUser):
    username = None 
    first_name = None
    last_name = None
    email = models.EmailField(_('email_address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email