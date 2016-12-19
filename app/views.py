from flask import render_template
from app import app
import datetime

@app.route('/')
def home():
    return render_template('base.html')  # render a template

@app.route('/talpacket')
def talpacket():
    return render_template('talpacket.html',  title='Is Tal\'s Door Open?')  # render a template

@app.route('/schedule')
def schedule():
    weekday = datetime.datetime.today().weekday()
    print ('hello {}'.format(weekday))
    return render_template('schedule.html', day=weekday)  # render a template