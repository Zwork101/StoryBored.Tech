from gevent.monkey import patch_all; patch_all()

from random import randint, uniform

from replit import db

from flask import Flask, render_template, send_file, redirect
from gevent.server import WSGIServer
from json2html import json2html
import numpy as np
import requests


app = Flask(__name__)

vids = np.load('vids.npy').tolist()

visits = db.get('visits', 0)

@app.after_request
def after_request():
  visits += 1
  db['visits'] = visits

@app.route('/')
def index():
  return render_template('index/index.html', visits=visits)

@app.route('/landscape')
def landscape():
  filea = open('unfinished/landscape/1.uhtml', 'r')
  a = filea.read()
  fileb = open('unfinished/landscape/2.uhtml', 'r')
  b = fileb.read()
  rand = randint(1, 17)
  if len(str(rand)) < 2:
    rand = '0' + str(rand)
  else: 
    rand = str(rand)
  return a + rand + b
	
@app.route('/img/<string:id>')
def returnIMG(id):
  filename = 'images/' + id + '.jpg'
  return send_file(filename, mimetype='image/gif')

@app.route('/video')
def returnvideo():
  v_id = vids[randint(0, 6899)] 
  return redirect("https://www.youtube.com/watch?v=" + v_id, code=302)

@app.route('/favicon.ico')
def favicon():
  return send_file('favicon.ico', mimetype='image/gif')

@app.route('/info')
def info():
  return render_template('info.html')

@app.route('/info/us')
def info_us():
  yeet = requests.get("https://corona.lmao.ninja/states").content.decode("utf-8")
  ok = json2html.convert(json = yeet)
  ok = ok.replace("state", "State")
  ok = ok.replace("cases", "Cases")
  ok = ok.replace("todayCases", "Cases Today")
  ok = ok.replace("deaths", "Deaths")
  ok = ok.replace("todayDeaths", "Deaths Today")
  ok = ok.replace("recovered", "Recovered")
  ok = ok.replace("active", "Active Cases")
  return '<html><head><title>US Statistics</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.min.css"></head><body><center>' + ok + '</center></body></html>'

@app.route('/info/world')
def info_world():
  yeet = requests.get("https://corona.lmao.ninja/jhucsse").content.decode("utf-8")
  ok = json2html.convert(json = yeet)
  ok = ok.replace("country", "Country")
  ok = ok.replace("province", "Most Affected Province")
  ok = ok.replace("updatedAt", "Last Time Updated")
  ok = ok.replace("stats", "Statistics")
  ok = ok.replace("confirmed", "Confirmed Cases")
  ok = ok.replace("deaths", "Deaths")
  ok = ok.replace("recovered", "Recovered Cases")
  ok = ok.replace("coordinates", "Coordinates of Country")
  ok = ok.replace("latitude", "Latitude")
  ok = ok.replace("longitude", "Longitude")
  return '<html><head><title>World Statistics</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.min.css"></head><body><center>' + ok + '</center></body></html>'

@app.route('/animal')
def animal():
  return render_template('animal.html')

@app.route('/robots.txt')
def robots():
  return "User-agent: * Disallow: "

@app.route('/place')
def place():
  randx = uniform(-90, 90)
  randy = uniform(-180, 180)
  return redirect("https://www.google.com/maps/@" + str(randx) + ',' + str(randy) + ',14z', code=302)

if __name__ == '__main__':
  WSGIServer(("0.0.0.0", 8080), app).run_forever()