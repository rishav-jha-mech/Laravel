# Generated by Django 3.2 on 2021-05-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_blog_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='blog_thumbnails/%Y/%m/%d/'),
        ),
    ]
