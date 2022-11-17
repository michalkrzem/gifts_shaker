from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# Create your models here.
class Gifts(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.URLField()
    author_id = models.ForeignKey(
        # settings.AUTH_USER_MODEL,
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
