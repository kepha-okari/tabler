
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt


class Schedule(models.Model):
    day = models.DateField(default=True)
    course = models.CharField(max_length = 10,blank =True)
    year1 = models.IntegerField(blank =True)
    year2 = models.IntegerField(blank =True)
    year3 = models.IntegerField(blank =True)
    year4 = models.IntegerField(blank =True)
    period = models.CharField(max_length = 10,blank =True)
    room = models.CharField(max_length = 10,blank =True)


    @classmethod
    def get_schedules(cls):
        schedules = cls.objects.all()
        return schedules

    @classmethod
    def get_specific_schedule(cls):
        schedules = cls.objects.filter()
        return schedules
