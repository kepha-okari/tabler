from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^table/record/',views.create_table,name='CreateTable'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]
