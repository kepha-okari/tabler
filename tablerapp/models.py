from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt


class Schedule(models.Model):
    day = models.DateField(default=True)
    course = models.CharField(max_length = 10,blank =True)
    year_of_study = models.CharField(max_length = 10,blank =True)
    period = models.CharField(max_length = 10,blank =True)
    room = models.CharField(max_length = 10,blank =True)


    @classmethod
    def get_schedules(cls):
        schedules = cls.objects.filter(Availability=True)
        return schedules

    @classmethod
    def get_booked_vacancies(cls):
        schedules = cls.objects.filter(Availability=False)
        return schedules
