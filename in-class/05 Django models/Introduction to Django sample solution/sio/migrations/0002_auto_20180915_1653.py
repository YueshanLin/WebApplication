# Generated by Django 2.1.1 on 2018-09-15 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='SecondName',
            new_name='LastName',
        ),
    ]