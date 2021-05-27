# Generated by Django 3.0.5 on 2021-05-26 17:43

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20210526_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('savings', 'SAVINGS'), ('current', 'CURRENT')], default='SAVINGS', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='D.O.B'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_activated',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport',
            field=models.FileField(null=True, upload_to=Users.models.User.get_path),
        ),
    ]