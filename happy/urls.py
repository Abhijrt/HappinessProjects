from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contactus',views.contactus,name='contactus'),
    path('event',views.createevent,name='event'),
    path('eventcreated',views.eventcreated,name='eventcreated'),
    path('notification',views.notification,name='notification'),
    path('accept',views.accept,name='accept')
]