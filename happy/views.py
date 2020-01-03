from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from .models import Created_event,Accepted_event
import datetime

def notification(request):
    eventcheck = Created_event.objects.filter(city='Indore')
    return render(request,'happy/notification.html',{'eventcheck':eventcheck})

def accept(request):
    f_name = request.user.first_name
    email = request.user.email
    user1 = Accepted_event(first_name=f_name,email=email)
    user1.save()

    return render(request,'happy/accept.html')


def index(request):
    return render(request,'happy/index.html')

def contactus(request):
    return render(request,'happy/contactus.html')

def createevent(request):
    if request.method=='POST':
        date=request.POST['date']
        type_of_event=request.POST['type_of_event']
        city=request.POST['city']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone_no=request.POST['phone_no']
        address=request.POST['address']
        description=request.POST['description']
        user_id_creater=request.user
        create=Created_event(date=date,type_of_event=type_of_event,city=city,first_name=first_name,last_name=last_name,address=address,description=description,phone_no=phone_no,user_id_creater=user_id_creater)
        create.save()
        return redirect('/eventcreated')
    else:
        return render(request,'happy/event.html')

def eventcreated(request):
    return render(request,'happy/eventcreated.html')


