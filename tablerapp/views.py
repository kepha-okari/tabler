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

    if request.method == 'POST':
            form = ScheduleForm(request.POST,request.FILES)

            if form.is_valid():
                day = form.cleaned_data['day']
                course = form.cleaned_data['course']
                # year1 = form.cleaned_data['year1']
                # year2 = form.cleaned_data['year2']
                # year3 = form.cleaned_data['year3']
                # year4 = form.cleaned_data['year4']
                period = form.cleaned_data['period']
                room1 = form.cleaned_data['room1']
                room2 = form.cleaned_data['room2']
                room3 = form.cleaned_data['room3']
                room4 = form.cleaned_data['room4']
                form1 = Schedule(day = day, course = course, year1 = '1', year2 ='2' ,year3 = '3' ,year4 = '4',period = period ,room1 = room1,room2 = room2,room3 = room3,room4 = room4)
                form1.save()
                return redirect(index)

    else:
        form = ScheduleForm()
    return render(request, 'create-table.html',{"form":form})


# @login_required(login_url='/accounts/login/')
def view_schedule(request):
    title = 'Timetable'
    schedules = Schedule.get_schedules()
    return render(request, 'view-schedule.html', { "title": title, "schedules":schedules})
