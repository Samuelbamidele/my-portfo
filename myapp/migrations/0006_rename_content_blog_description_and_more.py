# Generated by Django 5.1.4 on 2024-12-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_blog_description_blog_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='images/blog-img1.png', null=True, upload_to='blog_images/'),
        ),
    ]
