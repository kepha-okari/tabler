from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Schedule,Unit,Lecturer,Assign
from .forms import ScheduleForm


from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.

def index(request):
    title = 'Timetable'
    return render(request, 'index.html', {"title":title})


def add_unit(request):
    title = 'Units'
    units = Unit.get_units
    if request.method == 'POST':
        unit = request.POST['unit']
        code = request.POST['code']
        record = Unit(name = unit, code = code)
        record.save()
        return redirect(add_unit)

    return render(request, 'manage_unit.html', {"title":title, "units":units})

def delete_unit(request,unit_id):
    unit = Unit.objects.filter(id = unit_id)
    unit.delete()
    return redirect(add_unit)

def assign_unit(request,unit_id,lecturer_id):
    title = None
    unit = Unit.objects.get(id=unit_id)
    unit.assigned = True
    unit.save()
    assign = Assign(lecturer = lecturer_id, unit = unit_id)
    return redirect(lecturer_details, unit_id)

def add_lecturer(request):
    title = 'Lecturers'
    lecturers = Lecturer.get_lecturers
    if request.method == 'POST':
        lec = request.POST['lecturer']
        receive = Lecturer(name = lec)
        receive.save()
        return redirect(add_lecturer)
    return render(request, 'manage_lecturer.html', {"title":title,"lecturers":lecturers})

def lecturer_details(request,lecturer_id):
    lecturer = Lecturer.get_specific_lecturer(lecturer_id)
    title = None
    units = Unit.get_unassigned_units
    return render(request, 'lecturer-details.html', {"title":title,"lecturer":lecturer, "units":units,"lecturer_id":lecturer_id})

def delete_lecturer(request,lecturer_id):
    title = 'Lecturers'
    lecturer = Lecturer.objects.filter(id = lecturer_id)
    lecturer.delete()
    return redirect(add_lecturer)

def create_table(request):
    if request.method == 'POST':
        day = request.POST['day']
        period = request.POST['period']
        course = request.POST['course']
        room1 = request.POST['room-one']
        room2 = request.POST['room-two']
        room3 = request.POST['room-three']
        room4 = request.POST['room-four']
        unit1= request.POST['unit-one']
        unit2 = request.POST['unit-two']
        unit3 = request.POST['unit-three']
        unit4 = request.POST['unit-four']

        form = Schedule( day =day,
                         course = course,
                         year1 = '1', year2 ='2', year3 = '3', year4 = '4',
                         period = period,
                         room1 = room1, room2 = room2, room3 = room3,room4 = room4,
                         unit1 =unit1, unit2 =unit2, unit3 = unit3, unit4 =unit4
                       )

        form.save()
        return redirect(index)
    return render(request, 'create-table.html')



                # COMPUTER TECHNOLOGY

def view_schedule_ctec(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'ct', day = 'mon', year1 = 1)
    tues = Schedule.objects.filter(course = 'ct', day = 'tue', year1 = 1)
    weds = Schedule.objects.filter(course = 'ct', day = 'wed', year1 = 1)
    thus = Schedule.objects.filter(course = 'ct', day = 'thu', year1 = 1)
    fris = Schedule.objects.filter(course = 'ct', day = 'fri', year1 = 1)
    course = 'computer technology'
    year = 'first year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_ctec2(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'ct', day = 'mon', year2 = 2)
    tues = Schedule.objects.filter(course = 'ct', day = 'tue', year2 = 2)
    weds = Schedule.objects.filter(course = 'ct', day = 'wed', year2 = 2)
    thus = Schedule.objects.filter(course = 'ct', day = 'thu', year2 = 2)
    fris = Schedule.objects.filter(course = 'ct', day = 'fri', year2 = 2)
    course = 'computer technology'
    year = 'second year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_ctec3(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'ct', day = 'mon', year3 = 3)
    tues = Schedule.objects.filter(course = 'ct', day = 'tue', year3 = 3)
    weds = Schedule.objects.filter(course = 'ct', day = 'wed', year3 = 3)
    thus = Schedule.objects.filter(course = 'ct', day = 'thu', year3 = 3)
    fris = Schedule.objects.filter(course = 'ct', day = 'fri', year3 = 3)
    course = 'computer technology'
    year = 'third year '
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_ctec4(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'ct', day = 'mon', year4 = 4)
    tues = Schedule.objects.filter(course = 'ct', day = 'tue', year4 = 4)
    weds = Schedule.objects.filter(course = 'ct', day = 'wed', year4 = 4)
    thus = Schedule.objects.filter(course = 'ct', day = 'thu', year4 = 4)
    fris = Schedule.objects.filter(course = 'ct', day = 'fri', year4 = 4)
    course = 'computer technology'
    year = 'fourth year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})



                # COMPUTER NETWORKS

def view_schedule_cnet(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'cn', day = 'mon', year1 = 1)
    tues = Schedule.objects.filter(course = 'cn', day = 'tue', year1 = 1)
    weds = Schedule.objects.filter(course = 'cn', day = 'wed', year1 = 1)
    thus = Schedule.objects.filter(course = 'cn', day = 'thu', year1 = 1)
    fris = Schedule.objects.filter(course = 'cn', day = 'fri', year1 = 1)
    course = 'computer networks'
    year = 'first year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_cnet2(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'cn', day = 'mon', year2 = 2)
    tues = Schedule.objects.filter(course = 'cn', day = 'tue', year2 = 2)
    weds = Schedule.objects.filter(course = 'cn', day = 'wed', year2 = 2)
    thus = Schedule.objects.filter(course = 'cn', day = 'thu', year2 = 2)
    fris = Schedule.objects.filter(course = 'cn', day = 'fri', year2 = 2)
    course = 'computer networks'
    year = 'second year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_cnet3(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'cn', day = 'mon', year3 = 3)
    tues = Schedule.objects.filter(course = 'cn', day = 'tue', year3 = 3)
    weds = Schedule.objects.filter(course = 'cn', day = 'wed', year3 = 3)
    thus = Schedule.objects.filter(course = 'cn', day = 'thu', year3 = 3)
    fris = Schedule.objects.filter(course = 'cn', day = 'fri', year3 = 3)
    course = 'computer networks'
    year = 'third year '
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_cnet4(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'cn', day = 'mon', year4 = 4)
    tues = Schedule.objects.filter(course = 'cn', day = 'tue', year4 = 4)
    weds = Schedule.objects.filter(course = 'cn', day = 'wed', year4 = 4)
    thus = Schedule.objects.filter(course = 'cn', day = 'thu', year4 = 4)
    fris = Schedule.objects.filter(course = 'cn', day = 'fri', year4 = 4)
    course = 'computer networks'
    year = 'fourth year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

                # INFORMATION TECHNOLOGY

def view_schedule_infotec(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'it', day = 'mon', year1 = 1)
    tues = Schedule.objects.filter(course = 'it', day = 'tue', year1 = 1)
    weds = Schedule.objects.filter(course = 'it', day = 'wed', year1 = 1)
    thus = Schedule.objects.filter(course = 'it', day = 'thu', year1 = 1)
    fris = Schedule.objects.filter(course = 'it', day = 'fri', year1 = 1)
    course = 'information technology'
    year = 'first year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_infotec2(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'it', day = 'mon', year2 = 2)
    tues = Schedule.objects.filter(course = 'it', day = 'tue', year2 = 2)
    weds = Schedule.objects.filter(course = 'it', day = 'wed', year2 = 2)
    thus = Schedule.objects.filter(course = 'it', day = 'thu', year2 = 2)
    fris = Schedule.objects.filter(course = 'it', day = 'fri', year2 = 2)
    course = 'information technology'
    year = 'second year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_infotec3(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'it', day = 'mon', year3 = 3)
    tues = Schedule.objects.filter(course = 'it', day = 'tue', year3 = 3)
    weds = Schedule.objects.filter(course = 'it', day = 'wed', year3 = 3)
    thus = Schedule.objects.filter(course = 'it', day = 'thu', year3 = 3)
    fris = Schedule.objects.filter(course = 'it', day = 'fri', year3 = 3)
    course = 'information technology'
    year = 'third year '
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})

def view_schedule_infotec4(request):
    title = 'Timetable'
    mons = Schedule.objects.filter(course = 'it', day = 'mon', year4 = 4)
    tues = Schedule.objects.filter(course = 'it', day = 'tue', year4 = 4)
    weds = Schedule.objects.filter(course = 'it', day = 'wed', year4 = 4)
    thus = Schedule.objects.filter(course = 'it', day = 'thu', year4 = 4)
    fris = Schedule.objects.filter(course = 'it', day = 'fri', year4 = 4)
    course = 'information technology'
    year = 'fourth year'
    return render(request, 'view-schedule.html', { "title": title, "course":course, "year":year, "mons":mons, "tues":tues, "weds":weds, "thus":thus, "fris":fris})
