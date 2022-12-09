from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()
    author_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Invitation(models.Model):
    email = models.EmailField(null=True)
    accepted = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return f"{self.email}: {self.accepted}"


class Shaker(models.Model):
    shaker_name = models.CharField(max_length=50, null=True)
    user_in_shake = models.ManyToManyField(User)

    def __str__(self):
        return self.shaker_name
