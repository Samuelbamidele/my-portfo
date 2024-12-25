# Generated by Django 5.1.4 on 2024-12-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_about_aboutme'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='link',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='resume',
            field=models.FileField(default='Not providede', upload_to='resumes/'),
        ),
    ]
