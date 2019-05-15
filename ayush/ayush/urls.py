"""aditya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from  . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'index/',views.index, name="home"),
    url(r'^register/', views.register, name="register"),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    url(r'speakers/',views.speakers, name="speakers"),
    url(r'contact/', views.contact, name="contact"),
    url(r'events/', views.events, name="events"),
    url(r'dbput/', views.dbput, name="dbput"),
    url(r'insert_event/', views.insert_event, name="insert_event"),
    url(r'barcode/', views.barcode, name="barcode"),
    url(r'insert_test/', views.insert_test, name="insert_test"),
    url(r'test/', views.render_test, name="render_test"),
    url(r'insert_event/', views.insert_event, name="insert_event"),
    url(r'show_event/', views.show_event, name="show_event"),
    url(r'render_event_form/', views.render_event_form, name="render_event_form"),
    url(r'reserve/',views.reserve, name="reserve"),
    url(r'add_attendee/',views.add_attendee, name="add_attendee"),
    url(r'scan/', views.scan, name="scan"),

]
