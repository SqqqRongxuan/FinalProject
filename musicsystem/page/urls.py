"""page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('adminlogin', views.adminlogin),
    path('admin', views.admin),
    path('admin/gettop', views.gettop),
    path('admin/getlx', views.getlx),
    path('admin/getlxtop', views.getlxtop),
    path('adminallmusic', views.adminallmusic),
    path('admindel', views.admindel),
    path('adminadd', views.adminadd),
    path('adminuser', views.adminuser),
    path('admindeluser', views.admindeluser),
    path('getlink', views.getlink),
    path('', views.index),
    path('songdata', views.songdata),
    path('login', views.login),
    path('res', views.res),
    path('userindex', views.userindex),
    path('getuserinfo', views.getuserinfo),
    path('bangdinguserinfo', views.bangdinguserinfo),
    path('userinfoindex', views.userinfoindex),
    path('usersc', views.usersc),
    path('userdel', views.userdel),
    path('userplay', views.userplay),
    path('userclean', views.userclean),
    path('songindex', views.songindex),
    path('seach', views.seach),
    path('concert', views.concert),
    path('concertinfo', views.concertinfo),
    path('paihang', views.paihang),
    path('getallsongdata', views.getallsongdata),
    path('signin', views.signin),
    path('signup', views.signup)
]
