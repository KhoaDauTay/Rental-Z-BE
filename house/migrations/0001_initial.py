# Generated by Django 3.2.8 on 2021-10-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, unique=True)),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('property', models.CharField(choices=[('house', 'House'), ('flat', 'Flat'), ('bungalow', 'Bungalow')], max_length=20)),
                ('bed_rooms', models.CharField(choices=[('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('studio', 'Studio')], max_length=20)),
                ('furniture', models.CharField(blank=True, choices=[('house', 'Furnished'), ('flat', 'Unfurnished'), ('part furnished', 'Part Furnished')], max_length=20, null=True)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('create_at', models.DateField()),
                ('notes', models.TextField(blank=True, default='', max_length=200)),
                ('name_reporter', models.CharField(blank=True, default='', max_length=20)),
                ('is_best_offer', models.BooleanField(blank=True, default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
