# Generated by Django 2.2.2 on 2019-07-19 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190719_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.PNG', upload_to='profile_pics/%Y/%m/%d/'),
        ),
    ]
