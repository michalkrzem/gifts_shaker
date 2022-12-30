# Generated by Django 4.1.3 on 2022-12-30 22:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gifts', '0016_remove_pairs_unique_migration_host_combination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swhaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shaker_name', models.CharField(max_length=50, null=True)),
                ('owner', models.IntegerField(null=True)),
                ('user_in_shake', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
