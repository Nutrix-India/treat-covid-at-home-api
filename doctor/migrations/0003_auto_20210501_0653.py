# Generated by Django 3.2 on 2021-05-01 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctorstats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorstats',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
        migrations.AlterField(
            model_name='education',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
    ]
