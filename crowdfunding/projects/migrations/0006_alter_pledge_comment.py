# Generated by Django 5.1 on 2025-02-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_pledge_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
