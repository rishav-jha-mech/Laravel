# Generated by Django 3.2 on 2021-05-17 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_vlog_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('blogtitle', models.TextField(default='', max_length=300)),
                ('name', models.TextField(default='Anonymous', max_length=300)),
                ('blogsubtitle', models.TextField(default='', max_length=200)),
                ('blogcontent', models.TextField(default='')),
                ('pub_date', models.DateField(null=True)),
                ('thumbnail', models.ImageField(default='', upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Vlog',
        ),
    ]
