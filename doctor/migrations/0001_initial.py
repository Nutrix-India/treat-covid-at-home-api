# Generated by Django 3.2 on 2021-04-25 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('work_start_time', models.TimeField()),
                ('work_end_time', models.TimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('consultation_charge', models.FloatField(default=0)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('medical_registration_number', models.CharField(max_length=50)),
                ('working_days', models.CharField(max_length=7)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('lat', models.DecimalField(decimal_places=9, max_digits=20)),
                ('long', models.DecimalField(decimal_places=9, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('university_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doctor.doctor')),
            ],
        ),
    ]