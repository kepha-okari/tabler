from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Schedule


#*************************************************************************************************************

DAY_CHOICES = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday,
    ('friday', 'Friday'),
    ]

COURSE_CHOICES = [
    ('cn', 'Computer Networks'),
    ('ct', 'Computer Technology'),
    ('it', 'Information Technology'),
    ]
# PERIOD_CHOICES = [
#     ('cn', 'Computer Networks'),
#     ('ct', 'Computer Technology'),
#     ('it', 'Information Technology'),
#     ]


#********************************************************************************************************

class ScheduleForm(forms.Form):
    '''
    class that generates a new schedule
    '''
    day = models.DateField(default=True)
    course = models.CharField((label='course', widget=forms.RadioSelect(choices=COURSE_CHOICES)))
    year_of_study = models.CharField(max_length = 10,blank =True)
    period = models.CharField(max_length = 10,blank =True)
    room = models.CharField(max_length = 10,blank =True)
#
#
#
# class ProductForm(forms.Form):
#     '''
#     class that generates the Product creation form
#     '''
#     title = forms.CharField(label='Title',max_length = 50)
#     isbn = forms.CharField(label='ISBN',max_length = 50)
#     category = forms.CharField(label='Category', widget=forms.Select(choices=CATEGORY_CHOICES))
#     author = forms.CharField(label='Author',max_length = 50)
#     publisher = forms.CharField(label='Publisher', widget=forms.Select(choices=PUBLISHER_CHOICES))
#     price = forms.IntegerField(label='price')
#     quantity = forms.CharField(label='Quantity',max_length = 50)
#     image = forms.ImageField(label='Image',max_length = 50)
#

#*************************************************************************************************************
# class ProfileForm(forms.ModelForm):
#     '''
#     Class to create a form for an authenticated user to update profile
#     '''
#     class Meta:
#         model = Profile
#         fields = ['profile_photo','name']
