# Generated by Django 4.1.3 on 2023-01-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_project', models.CharField(max_length=100, verbose_name='type_project')),
                ('size_project', models.SmallIntegerField(verbose_name='size_project')),
                ('company', models.CharField(max_length=100, verbose_name='company')),
                ('dates', models.BigIntegerField(blank=True, null=True, verbose_name='dates')),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('neighbourhood', models.CharField(max_length=100, null=True, verbose_name='neighbourhood')),
                ('value', models.FloatField(verbose_name='value')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('room', models.SmallIntegerField(verbose_name='room')),
                ('floor', models.FloatField(verbose_name='floor')),
                ('property_type', models.CharField(max_length=100, verbose_name='property_type')),
                ('street', models.CharField(max_length=100, verbose_name='street')),
                ('neighbourhood', models.CharField(max_length=100, verbose_name='neighbourhood')),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('price', models.BigIntegerField(verbose_name='price')),
            ],
        ),
    ]
