# Generated by Django 3.2.8 on 2021-10-28 14:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='book_marks',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), size=None), blank=True, default=[], null=True, size=None),
        ),
    ]
