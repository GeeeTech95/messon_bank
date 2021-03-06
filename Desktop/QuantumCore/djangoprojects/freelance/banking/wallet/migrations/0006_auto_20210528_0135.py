# Generated by Django 3.0.5 on 2021-05-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_auto_20210526_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='nature',
            field=models.CharField(choices=[('Withdrawal', 'Withdrawal'), ('Deposit', 'Deposit'), ('Transfer', 'Transfer')], max_length=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Failed', 'Failed'), ('Processing', 'Processing'), ('Successful', 'SuccessfulL')], max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Debit', 'Debit'), ('Dredit', 'Credit')], max_length=10),
        ),
    ]
