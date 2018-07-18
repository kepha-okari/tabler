from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Schedule,Unit,Lecturer,Assign,Profile
from .forms import ScheduleForm


from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    title = 'Timetable'
    current_user = request.user
    profile = Profile.get_profile(current_user.id)

    return render(request, 'index.html', {"title":title,"profile":profile})


@login_required(login_url='/accounts/login')
def update_profile(request):
    title = 'Profile'
    current_user = request.user
    profile = Profile.get_profile(current_user.id)

    if request.method == 'POST':
        status = request.POST['level']
        email = request.POST['mail']
        phone = request.POST['phone']
        remove = Profile.objects.filter(user = request.user.id)
        remove.delete()
        record, created = Profile.objects.get_or_create( user = current_user, user_type = status, email = email, phone_number = phone )
        record.save()
        return redirect(index)
    # profile = Profile.get_profile(current_user.id)
    return render(request, 'update-profile.html', { "title": title,"profile": profile})


@login_required(login_url='/accounts/login')
def add_unit(request):
    title = 'Units'
    units = Unit.get_units
    profile = Profile.objects.filter(user = request.user.id)

    if request.method == 'POST':
        unit = request.POST['unit']
        code = request.POST['code']
        record = Unit(name = unit, code = code)
        record.save()
        return redirect(add_unit)

    return render(request, 'manage_unit.html', {"title":title, "units":units,"profile": profile})

@login_required(login_url='/accounts/login')
def delete_unit(request,unit_id):
    unit = Unit.objects.filter(id = unit_id)
    unit.delete()
    return redirect(add_unit)

@login_required(login_url='/accounts/login')
def assign_unit(request,unit_id,lecturer_id):
    title = None
    # profile = Profile.get_profile(request.user.id)
    unit = Unit.objects.get(id=unit_id)
    unit.assigned = True
    unit.save()
    assign = Assign.assign_unit(int(lecturer_id), int(unit_id))

    return redirect(lecturer_details, lecturer_id)

@login_required(login_url='/accounts/login')
def add_lecturer(request):
    title = 'Lecturers'
    profile = Profile.objects.filter(user = request.user.id)
    lecturers = Lecturer.get_lecturers
    if request.method == 'POST':
        lec = request.POST['lecturer']
        receive = Lecturer(name = lec)
        receive.save()
        return redirect(add_lecturer)
    return render(request, 'manage_lecturer.html', {"title":title,"lecturers":lecturers,"profile": profile})

@login_required(login_url='/accounts/login')
def unit_details(request,unit_code):
    title = 'Unit'
    profile = Profile.get_profile(request.user.id)

    try:
        unit = Unit.get_specific_unit(unit_code)
        lec = Assign.objects.get(unit = unit.id)
        lecturer = Lecturer.get_specific_lecturer(lec.lecturer)
        unit_status = True
    except ObjectDoesNotExist:
        unit = 'value not present'
        lecturer = 'not present yet'
        unit_status = False

    return render(request, 'unit-details.html', {"title":title,"lecturer":lecturer, "unit":unit,"profile": profile})


@login_required(login_url='/accounts/login')
def lecturer_details(request,lecturer_id):
    lecturer = Lecturer.get_specific_lecturer(lecturer_id)
    title = None
    profile = Profile.get_profile(request.user.id)

    units = Unit.get_unassigned_units
    assignments = Assign.objects.filter(lecturer = lecturer_id)
    allocations = [Unit.objects.filter(id=i.unit)[0] for i in assignments][::-1][:4]

    if allocations:
        allocations_status = True
    else: allocations_status = False

    counter = len(allocations)
    if counter < 4:
        count_status = False
    else:count_status = True

    return render(request, 'lecturer-details.html', {"title":title,"lecturer":lecturer, "count_status":count_status, "units":units,"lecturer_id":lecturer_id,"allocations":allocations,"allocations_status":allocations_status,"profile": profile})

@login_required(login_url='/accounts/login')
def relieve_unit(request,unit_id,lecturer_id):
    title = 'Lecturers'
    # remove = Assign.objects.get(id = Assign.objects.filter(unit = unit_id).first().id)
    unassign_unit = Assign.objects.filter(unit = unit_id).first()
    remove = Assign.objects.get(id = Assign.objects.filter(unit = unit_id).first().id)
    remove.delete()
    return redirect(lecturer_details, lecturer_id)


@login_required(login_url='/accounts/login')
def lecturer_schedule(request,lecturer_id):
    title = 'Lecturer Schedule'
    profile = Profile.get_profile(request.user.id)
    assigns = Assign.objects.filter(lecturer = lecturer_id)
    unit_ids = [assigned.unit for assigned in assigns]

    unit_codes = [Unit.objects.get(id = unit_id).code for unit_id in unit_ids]

    first = [Schedule.objects.filter( unit1 = unit_code ) for unit_code in unit_codes]
    second = [Schedule.objects.filter( unit2 = unit_code ) for unit_code in unit_codes]
    third = [Schedule.objects.filter( unit3 = unit_code ) for unit_code in unit_codes]
    fourth = [Schedule.objects.filter( unit4 = unit_code ) for unit_code in unit_codes]

    return render(request, 'lecturer-schedule.html', { "title": title, "first":first, "second":second, "third":third, "fourth":fourth, "profile":profile })

@login_required(login_url='/accounts/login')
def delete_lecturer(request,lecturer_id):
    title = 'Lecturers'
    lecturer = Lecturer.objects.filter(id = lecturer_id)
    lecturer.delete()
    return redirect(add_lecturer)



@login_required(login_url='/accounts/login')
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

        form, created = Schedule.objects.get_or_create(
                         day =day,
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
