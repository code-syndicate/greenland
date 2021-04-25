# Generated by Django 3.1.6 on 2021-04-24 17:35

import banking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='account_number',
            field=models.BigIntegerField(default=banking.models.generate_acct_num, max_length=25),
        ),
    ]
