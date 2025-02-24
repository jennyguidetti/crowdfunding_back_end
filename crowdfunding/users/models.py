from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    employer = models.CharField(max_length=100, blank=True, null=True)
    clinical_level = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username" 
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username