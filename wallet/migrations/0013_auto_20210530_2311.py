# Generated by Django 3.0.5 on 2021-05-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0012_transaction_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='bank_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]