# Generated by Django 3.0.5 on 2021-05-31 11:15

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20210528_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_number',
            field=models.CharField(blank=True, default=Users.models.User.get_account_number, max_length=14, unique=True),
        ),
    ]
