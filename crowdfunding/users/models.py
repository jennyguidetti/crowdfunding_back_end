from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    employer = models.CharField(max_length=50)
    clinical_level = models.CharField(max_length=50)

    def __str__(self):
        return self.username