# Generated by Django 4.2.3 on 2023-07-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0003_user_is_superuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(null=True, upload_to="media/img"),
        ),
    ]