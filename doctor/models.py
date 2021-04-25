from django.db import models


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    consultation_charge = models.FloatField(default=0)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    medical_registration_number = models.CharField(max_length=50)
    working_days = models.CharField(max_length=7)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    lat = models.DecimalField(decimal_places=9, max_digits=20)
    long = models.DecimalField(decimal_places=9, max_digits=20)


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.IntegerField()
    doctor = models.ForeignKey(to='Doctor', on_delete=models.PROTECT)


class Education(models.Model):
    id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    doctor = models.ForeignKey(to='Doctor', on_delete=models.PROTECT)
