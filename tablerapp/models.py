
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt

class Profile(models.Model):
    user_type = models.CharField(max_length=10,default='student')
    email = models.EmailField(max_length = 60,blank =True)
    phone_number = models.CharField(max_length = 10,blank =True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    @classmethod
    def get_profile(cls,user_id):
        profile = cls.objects.get(user=user_id)
        return profile

class Schedule(models.Model):
    day = models.CharField(max_length = 10,blank = True,null = True)
    course = models.CharField(max_length = 10,blank = True,null = True)
    period = models.CharField(max_length = 10,blank = True,null = True)
    year1 = models.IntegerField(blank = True,null = True)
    year2 = models.IntegerField(blank = True,null = True)
    year3 = models.IntegerField(blank = True,null = True)
    year4 = models.IntegerField(blank = True,null = True)
    room1 = models.CharField(max_length = 10,blank = True,null = True)
    room2 = models.CharField(max_length = 10,blank = True,null = True)
    room3 = models.CharField(max_length = 10,blank = True,null = True)
    room4 = models.CharField(max_length = 10,blank = True,null = True)
    unit1 = models.CharField(max_length = 10,blank = True,null = True)
    unit2 = models.CharField(max_length = 10,blank = True,null = True)
    unit3 = models.CharField(max_length = 10,blank = True,null = True)
    unit4 = models.CharField(max_length = 10,blank = True,null = True)


    @classmethod
    def get_schedules(cls):
        schedules = cls.objects.all()
        return schedules

    @classmethod
    def get_specific_course_schedule(cls, course):
        schedules = cls.objects.filter(course = course)
        return schedules


class Unit(models.Model):
    name = models.CharField(max_length = 20,blank = True)
    code = models.CharField(max_length = 10,blank = True)
    assigned = models.BooleanField(default=False)

    @classmethod
    def get_units(cls):
        units = cls.objects.all()
        return units

    @classmethod
    def get_specific_unit(cls, unit_code):
        unit = cls.objects.get(code = unit_code)
        return unit
    @classmethod
    def get_unassigned_units(cls):
        units = cls.objects.filter(assigned = False)
        return units


class Lecturer(models.Model):
    name = models.CharField(max_length = 20,blank = True)

    @classmethod
    def get_lecturers(cls):
        lecturers = cls.objects.all()
        return lecturers

    @classmethod
    def get_specific_lecturer(cls,lecturer_id):
        lecturer = cls.objects.get(id = lecturer_id)
        return lecturer


class Assign(models.Model):
    lecturer = models.IntegerField(blank = True,null = True)
    unit = models.IntegerField(blank = True,null = True)

    @classmethod
    def assign_unit(cls,lecturer,unit):
        record = Assign(lecturer = lecturer, unit = unit)
        record.save()
