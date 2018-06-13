from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from .models import Schedule
from .forms import ScheduleForm


from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.

def index(request):
    title = 'Timetable'
    return render(request, 'index.html', {"title":title})




def create_table(request):
    form = ScheduleForm()
    if request.method == 'POST':
            form = ScheduleForm(request.POST,request.FILES)

            if form.is_valid():
                day = form.cleaned_data['day']
                course = form.cleaned_data['course']
                year1 = form.cleaned_data['year1']
                year2 = form.cleaned_data['year2']
                year3 = form.cleaned_data['year3']
                year4 = form.cleaned_data['year4']
                period = form.cleaned_data['period']
                room = form.cleaned_data['room']

                form = Schedule(day = day, course =course ,year1 =year1,year2 =year2 ,year3 = year3 ,year4 = year4,period = period ,room = room)
                form.save()
                return redirect(home)

            else:
                form = ScheduleForm()
    return render(request, 'create-table.html',{"form":form})
