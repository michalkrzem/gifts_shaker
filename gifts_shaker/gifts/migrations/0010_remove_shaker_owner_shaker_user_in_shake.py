# Generated by Django 4.1.3 on 2022-12-08 14:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gifts', '0009_invitation_shaker_usershaker_rename_gifts_gift_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shaker',
            name='owner',
        ),
        migrations.AddField(
            model_name='shaker',
            name='user_in_shake',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
