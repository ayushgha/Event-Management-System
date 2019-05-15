from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie

from .forms import UserRegisterForm
import sqlite3
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def events(request):
    return render(request,"events.html")

def speakers(request):
    return render(request,"speakers.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for { username }!')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,"register.html",{'form':form})


def dbput(request):
    #conn = sqlite3.connect('SPIY_Event.sqlite3')
    #cur = conn.cursor()

    return render(request, "dbput.html")
#


def render_test(request):

    return render(request, "insert_event.html")


def insert_event(request):
    conn = sqlite3.connect('SPIT_Event.sqlite3')
    cur = conn.cursor()
    EventName = request.POST['EventName']
    AttendeesNo = request.POST['AttendeesNo']
    RoomNo = request.POST['RoomNo']
    EventDate = request.POST['EventDate']
    StartTime = request.POST['StartTime']
    EndTime = request.POST['EndTime']
    Description = request.POST['Description']
    FirstName = request.POST['FirstName']
    LastName = request.POST['LastName']

    cur.execute("insert into Events (EventName, AttendeesNo, RoomNo, EventDate, StartTime, EndTime, Description, FirstName, LastName) values (?,?,?,?,?,?,?,?,?)", (EventName, AttendeesNo, RoomNo, EventDate, StartTime, EndTime, Description, FirstName, LastName));
    conn.commit()

    # for i in cur.fetchall():
    #     print(i[0],i[1],i[2])
    cur.close()
    conn.close()


#     conn.close()
    return show_event(request)
#     return render(request,"index.html")

#
def show_event(request):
    conn = sqlite3.connect('SPIT_Event.sqlite3')
    cur = conn.cursor()
    cur.execute('select EventID,EventName, RoomNo, EventDate, StartTime, EndTime, Description from Events order by EventDate desc')

    context= {}

    count = 0
    for i in cur.fetchall():
        row = {}

        row['EventID'] = i[0]
        row['EventName'] = i[1]
        row['RoomNo'] = i[2]
        row['EventDate'] = i[3]
        row['StartTime'] = i[4]
        row['EndTime'] = i[5]
        row['Description'] = i[6]

        context[count]=row
        count=count+1


    #print(context)

    cur.close()
    conn.close()
    return render(request, "show_event.html", {"context":context})


def insert_test(request):
    Desc = request.POST['description']
    #print(Desc)

    return render(request, "insert.html")


def reserve(request):
    return render(request, "reserve.html")


def add_attendee(request):
    conn = sqlite3.connect('SPIT_Event.sqlite3')
    cur = conn.cursor()
    EventID = request.POST['EventID']
    Name = request.POST['name1']
    Contact = request.POST['contact1']
    Email = request.POST['email1']
    cur.execute(
        "insert into Attendees (Name, Contact, Email, EventID) values (?,?,?,?)",
        (Name, Contact, Email, EventID));
    conn.commit()
    cur.close()
    conn.close()
    return barcode(request)


def barcode(request):
    import cv2
    import pyqrcode
    from PIL import Image
    #from pyzbar.pyzbar import decode

    import re

    name = request.POST['name1']
    email = request.POST['email1']


    #print(name)




    #print(email, y[0])
    qr = pyqrcode.create(str(email))
    qr.png("test6.png", scale=6)
    filename = 'test6.png'
    return render(request,"bar_code.html")



def render_event_form(request):
    return render(request, "insert_event.html")


# def html_code_for_event(i):
#     file = open("/home/gayatri/PycharmProjects/gayatri/gayatri/templates/show_event.html", 'w')
#     str = '<!DOCTYPE html>\
#                 <html lang="en">\
#                 <head>\
#                 <meta charset="UTF-8">\
#                 <title></title>\
#                 </head>\
#                 <body>'
#     str += '<p>hello</p>'
#     for temp in i:
#         str += '<p>' + temp[0] + '</p>'
#     str += '</body></html>'
#     file.write(str)
#     file.close()



def scan(request):




    return render(request, "scan.html")