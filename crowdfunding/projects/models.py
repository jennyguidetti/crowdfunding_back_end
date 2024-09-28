from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )

# class User(models.Model):
#     title = models.CharField(max_length=10)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=40)
#     age = models.IntegerField()
#     employer = models.TextField()
#     clinical_level = models.TextField()
#     years_experience = models.CharField(max_length=20)
#     email = models.TextField()
#     phone_number = models.CharField(max_length=10)
#     postcode = models.CharField(max_length=10)
#     is_open = models.BooleanField()
#     date_created = models.DateTimeField(auto_now_add=True)