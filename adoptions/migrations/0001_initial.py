# Generated by Django 3.2.12 on 2022-02-16 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=30)),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField()),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('submission_date', models.DateTimeField()),
                ('age', models.IntegerField(null=True)),
                ('submitter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adoptions.submitter')),
                ('vaccinations', models.ManyToManyField(blank=True, to='adoptions.Vaccine')),
            ],
        ),
    ]