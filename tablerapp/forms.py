from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Schedule


#*************************************************************************************************************

DAY_CHOICES = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ]

COURSE_CHOICES = [
    ('cn', 'Computer Networks'),
    ('ct', 'Computer Technology'),
    ('it', 'Information Technology'),
    ]

PERIOD_CHOICES = [
    ('7', '7 - 9 AM'),
    ('9', '9 - 11 AM'),
    ('11','11 - 1 AM'),
    ('2', '2 - 4 AM'),
    ('2', '4 - 6 AM'),
    ]


#********************************************************************************************************

class ScheduleForm(forms.Form):
    '''
    class that generates a new schedule
    '''
    day = forms.ChoiceField(choices=DAY_CHOICES,widget=forms.RadioSelect())
    course = forms.ChoiceField(choices=COURSE_CHOICES,widget=forms.RadioSelect())
    period = forms.ChoiceField(choices=PERIOD_CHOICES,widget=forms.RadioSelect())
#   year1 = forms.IntegerField()
#     year2 = forms.IntegerField()
#     year3 = forms.IntegerField()
#     year4 = forms.IntegerField()
    room1 = forms.CharField(max_length = 10)
    room2 = forms.CharField(max_length = 10)
    room3 = forms.CharField(max_length = 10)
    room4 = forms.CharField(max_length = 10)


#*************************************************************************************************************
