# Generated by Django 2.2.5 on 2019-11-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='username',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='info',
            name='password',
            field=models.CharField(max_length=16),
        ),
    ]
