from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^table/record/',views.create_table,name='CreateTable'),
    url(r'^manage/unit/',views.add_unit,name='AddUnit'),
    url(r'^remove/unit/(\d+)',views.delete_unit,name='DeleteUnit'),
    url(r'^assign/unit/(\d+)/([0-9]+)',views.assign_unit,name='AssignUnit'),
    url(r'^manage/lecturer/',views.add_lecturer,name='AddUnit'),
    url(r'^remove/lecturer/(\d+)',views.delete_lecturer,name='DeleteLecturer'),
    url(r'^lecturer/details/(\d+)',views.lecturer_details,name='LecturerDetails'),


    url(r'^view/computer/technology/one', views.view_schedule_ctec, name='ViewSchedulesTec'),
    url(r'^view/computer/technology/two', views.view_schedule_ctec2, name='ViewSchedulesTec2'),
    url(r'^view/computer/technology/three', views.view_schedule_ctec3, name='ViewSchedulesTec3'),
    url(r'^view/computer/technology/four', views.view_schedule_ctec4, name='ViewSchedulesTec4'),

    url(r'^view/schedules/one', views.view_schedule_cnet, name='ViewSchedulesCnet'),
    url(r'^view/schedules/two', views.view_schedule_cnet2, name='ViewSchedulesCnet2'),
    url(r'^view/schedules/three', views.view_schedule_cnet3, name='ViewSchedulesCnet3'),
    url(r'^view/schedules/four', views.view_schedule_cnet4, name='ViewSchedulesCnet4'),

    url(r'^view/information/technology/one', views.view_schedule_infotec, name='ViewSchedulesInfoTech'),
    url(r'^view/information/technology/two', views.view_schedule_infotec2, name='ViewSchedulesInfoTech2'),
    url(r'^view/information/technology/three', views.view_schedule_infotec3, name='ViewSchedulesInfoTech3'),
    url(r'^view/information/technology/four', views.view_schedule_infotec4, name='ViewSchedulesInfoTech4'),

    url(r'^accounts/', include('registration.backends.simple.urls')),

]
