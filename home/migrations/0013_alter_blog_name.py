# Generated by Django 3.2 on 2021-05-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_blog_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.TextField(default='Anonymous', max_length=50),
        ),
    ]
