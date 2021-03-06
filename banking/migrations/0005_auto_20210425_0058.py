# Generated by Django 3.1.6 on 2021-04-24 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_transferrequest_transfer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferrequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined'), ('unverified', 'Awaiting Verification')], default='pending', max_length=25),
        ),
    ]
