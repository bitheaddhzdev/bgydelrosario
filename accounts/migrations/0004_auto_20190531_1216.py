# Generated by Django 2.2.1 on 2019-05-31 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190531_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]