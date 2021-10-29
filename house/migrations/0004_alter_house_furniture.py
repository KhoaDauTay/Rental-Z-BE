# Generated by Django 3.2.8 on 2021-10-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_housetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='furniture',
            field=models.CharField(blank=True, choices=[('furnished', 'Furnished'), ('unfurnished', 'Unfurnished'), ('part furnished', 'Part Furnished')], max_length=20, null=True),
        ),
    ]