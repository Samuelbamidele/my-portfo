# Generated by Django 5.1.4 on 2024-12-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='images/blog-img1.png', null=True, upload_to='blog_images/'),
        ),
    ]
