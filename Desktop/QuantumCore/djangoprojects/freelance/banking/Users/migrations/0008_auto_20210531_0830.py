# Generated by Django 3.0.5 on 2021-05-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20210531_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]
