# Generated by Django 2.1.1 on 2018-10-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181005_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
