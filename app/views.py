from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('base.html')  # render a template

@app.route('/talpacket')
def talpacket():
    return render_template('talpacket.html',  title='Is Tal\'s Door Open?')  # render a template

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')  # render a template