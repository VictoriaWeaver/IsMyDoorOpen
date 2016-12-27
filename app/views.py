from flask import render_template
from app import app
import datetime
from . import course

@app.route('/')
def home():
    return render_template('base.html')  # render a template

@app.route('/talpacket')
def talpacket():
    return render_template('talpacket.html',  title='Is Tal\'s Door Open?')  # render a template

@app.route('/schedule')
def schedule():
    # Classes in my schedule
    c1 = course.Course('CMPE-495','Senior Design',' 3:30pm-4:45pm')
    c2 = course.Course('CMPE-530','Digital IC Design','3:00pm-4:15pm')
    c3 = course.Course('CMPE-530 Lab','Digital IC Design','2:00pm-3:50pm')
    c4 = course.Course('CMPE-550','Computer Architecture','5:00pm-6:15pm')
    c5 = course.Course('CMPE-610','Analytical Topics','10:00am-11:50am')
    c6 = course.Course('CMPE-685','Computer Vision','1:00pm-2:50pm')

    # Classes for each day of the week (chronological order)
    mon = [c5, c6, c2, c4]
    tues = [c1]
    wed = [c5, c6, c2, c4]
    thurs = [c1]
    fri = [c3]
    sat = []
    sun = []

    # Dictionary for each day of the week
    dow = datetime.datetime.today().weekday()
    weekdays = { 0:mon,
                 1:tues,
                 2:wed,
                 3:thurs,
                 4:fri,
                 5:sat,
                 6:sun
                 }

    return render_template('schedule.html', day=dow, classes=weekdays[dow])  # render a template