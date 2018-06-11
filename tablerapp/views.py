from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.

def index(request):
    title = 'Timetable'
    return render(request, 'index.html', {})




def create_table(request):
    form = ScheduleForm()
    if request.method == 'POST':
            form = ScheduleForm(request.POST,request.FILES)

            if form.is_valid():
                day = form.cleaned_data['day']
                course = form.cleaned_data['course']
                year_of_study = form.cleaned_data['year_of_study']
                period = form.cleaned_data['period']
                room = form.cleaned_data['room']


                requested_prods = Schedule.create_table()
                return render(request, 'results.html',{"form":form,"table_inputs":table_inputs})
            else:
                form = ScheduleForm()
    return render(request, 'create-table.html',{"form":form})
