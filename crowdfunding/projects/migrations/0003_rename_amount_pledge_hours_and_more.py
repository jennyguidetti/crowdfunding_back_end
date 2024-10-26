# Generated by Django 5.1 on 2024-10-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge_supporter_project_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledge',
            old_name='amount',
            new_name='hours',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='organisation_description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='organisation_name',
            field=models.CharField(default='Ambulance Service', max_length=50),
            preserve_default=False,
        ),
    ]
