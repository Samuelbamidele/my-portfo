# Generated by Django 5.1.4 on 2024-12-24 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_about_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About',
            new_name='AboutMe',
        ),
    ]