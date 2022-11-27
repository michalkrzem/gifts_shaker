from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Gifts(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()
    author_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Shakers(models.Model):
    shaker_name = models.CharField(max_length=50, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    group_members = ArrayField(
        models.IntegerField()
    )

    def __str__(self):
        return self.shaker_name
