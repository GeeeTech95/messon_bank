# Generated by Django 3.0.5 on 2021-05-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_transaction_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='account_type',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(editable=False, max_length=20),
        ),
        migrations.DeleteModel(
            name='AccountType',
        ),
    ]
