# Generated by Django 4.1.3 on 2022-12-08 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0010_remove_shaker_owner_shaker_user_in_shake'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserShaker',
        ),
    ]
