# Generated by Django 3.1.6 on 2021-04-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=48, null=True),
        ),
    ]