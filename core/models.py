from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    book_marks = ArrayField(
        ArrayField(
            models.IntegerField(blank=True),
        ), null=True, blank=True, default=[]
    )
