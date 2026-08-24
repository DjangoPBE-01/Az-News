from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.accounts.manager import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True, verbose_name='Avatar', help_text='The filed is saved avatar.')
    email = models.EmailField(unique=True, verbose_name='Email', help_text='The filed is saved email.')
    
    
    objects = CustomUserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'


    def __str__(self)-> str:
        """_summary_

        Returns:
            str: _email
        """
        return self.email
