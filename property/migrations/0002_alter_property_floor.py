# Generated by Django 4.1.3 on 2023-01-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='floor',
            field=models.SmallIntegerField(verbose_name='floor'),
        ),
    ]
