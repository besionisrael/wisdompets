# Generated by Django 3.2.12 on 2022-02-16 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0002_vaccine_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='description',
        ),
    ]
