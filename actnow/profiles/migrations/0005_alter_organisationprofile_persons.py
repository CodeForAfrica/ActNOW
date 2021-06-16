# Generated by Django 3.2.3 on 2021-06-16 03:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("profiles", "0004_timestamp_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organisationprofile",
            name="persons",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
