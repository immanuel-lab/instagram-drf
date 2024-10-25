# Generated by Django 5.0.6 on 2024-07-01 04:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL),
        ),
    ]
