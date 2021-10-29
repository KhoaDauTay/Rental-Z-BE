from django.db import models

# Create your models here.
PROPERTIES = (
    ('house', 'House'),
    ('flat', 'Flat'),
    ('bungalow', 'Bungalow'),
)
BEDROOMS = (
    ('one', 'One'),
    ('two', 'Two'),
    ('three', 'Three'),
    ('studio', 'Studio'),
)
FURNITURE_TYPES = (
    ('furnished', 'Furnished'),
    ('unfurnished', 'Unfurnished'),
    ('part furnished', 'Part Furnished'),
)


class House(models.Model):
    name = models.CharField(max_length=50, default='', blank=True, unique=True)
    address = models.CharField(max_length=100, default='', null=True, blank=True)
    property = models.CharField(max_length=20, choices=PROPERTIES)
    bed_rooms = models.CharField(max_length=20, choices=BEDROOMS)
    furniture = models.CharField(max_length=20, choices=FURNITURE_TYPES, blank=True, null=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateField()
    notes = models.TextField(max_length=200, default='', blank=True)
    name_reporter = models.CharField(default='', max_length=20)
    is_best_offer = models.BooleanField(default=False, blank=True)
    image = models.ImageField(null=True, blank=True, default='')

    def __str__(self):
        return self.name + '-'+self.property.title()


class HouseType(models.Model):
    inside_property = models.TextField(max_length=200, default='', blank=True)
    outside_property = models.TextField(max_length=200, default='', blank=True)
    have_wifi = models.BooleanField(default=False)
    house = models.ForeignKey(
        House, on_delete=models.CASCADE,
    )
