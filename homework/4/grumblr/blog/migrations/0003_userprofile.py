# Generated by Django 2.1.1 on 2018-10-04 15:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20180922_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='')),
                ('age', models.CharField(max_length=3)),
                ('user', models.OneToOneField(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
