import os
from django.contrib.auth import get_user_model
from django.db import migrations


def create_superuser(apps, schema_editor):
    User = apps.get_model("users", "CustomUser")

    DJ_SU_USERNAME = os.environ.get("DJ_SU_USERNAME")
    DJ_SU_EMAIL = os.environ.get("DJ_SU_EMAIL")
    DJ_SU_PASSWORD = os.environ.get("DJ_SU_PASSWORD")


    User.objects.create_superuser(
        email=DJ_SU_EMAIL,
        username=DJ_SU_USERNAME,
        password=DJ_SU_PASSWORD
    )


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]