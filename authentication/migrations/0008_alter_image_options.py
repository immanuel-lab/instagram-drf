# Generated by Django 5.0.6 on 2024-07-01 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_delete_imageshare'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['owner']},
        ),
    ]