from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    organisation_name = models.CharField(max_length=100, unique=True)
    organisation_description = models.TextField(blank=True, null=True)
    goal = models.PositiveIntegerField(default=0)
    image = models.URLField(blank=True, null=True)
    is_open = models.BooleanField(default=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def total_pledges(self):
        return self.pledges.count()

class Pledge(models.Model):
    hours = models.PositiveIntegerField()
    comment = models.CharField(max_length=200, blank=True, null=True)
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