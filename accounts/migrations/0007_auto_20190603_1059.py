# Generated by Django 2.2.1 on 2019-06-03 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190603_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
