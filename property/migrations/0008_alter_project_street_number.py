# Generated by Django 4.1.3 on 2022-11-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0007_rename__id_property_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="street_number",
            field=models.SmallIntegerField(
                max_length=100, verbose_name="street_number"
            ),
        ),
    ]
