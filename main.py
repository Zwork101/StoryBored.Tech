from flask import Flask, render_template, send_file, redirect, jsonify, request
from random import randint, uniform
import numpy as np
import requests
from json2html import *
app = Flask('app')
vids = np.load('vids.npy').tolist()

@app.route('/')
def index():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return render_template('index/index.html')

@app.route('/landscape')
def landscape():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return compileLandscape()
	
@app.route('/img/<string:id>')
def returnIMG(id):
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	filename = 'images/' + id + '.jpg'
	return send_file(filename, mimetype='image/gif')

@app.route('/video')
def returnvideo():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	global vids
	id = getrandomvideo(vids)
	return redirect("https://www.youtube.com/watch?v=" + id, code=302)

@app.route('/favicon.ico')
def favicon():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return send_file('favicon.ico', mimetype='image/gif')

@app.route('/info')
def info():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return render_template('info.html')

@app.route('/info/us')
def info_us():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return get_us()

@app.route('/info/all')
def info_all():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return get_all()

@app.route('/info/world')
def info_world():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return get_world()

@app.route('/animal')
def animal():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return render_template('animal.html')

@app.route('/robots.txt')
def robots():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	return "User-agent: * Disallow: "

@app.route('/place')
def place():
	#requests.get('https://www.simple-counter.com/hit.php?id=zroxkx&nd=8&nc=4&bc=1')
	with open("test.txt","a+") as fo:
		fo.write(request.remote_addr)
	randx = uniform(-90, 90)
	randy = uniform(-180, 180)
	return redirect("https://www.google.com/maps/@" + str(randx) + ',' + str(randy) + ',14z', code=302)

def getrandomvideo(vids):
	return vids[randint(0, 6899)]

def compileLandscape():
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

def get_us():
	yeet = requests.get("https://corona.lmao.ninja/v2/states").content.decode("utf-8")
	ok = json2html.convert(json = yeet)
	ok = ok.replace("state", "State")
	ok = ok.replace("cases", "Cases")
	ok = ok.replace("todayCases", "Cases Today")
	ok = ok.replace("deaths", "Deaths")
	ok = ok.replace("todayDeaths", "Deaths Today")
	ok = ok.replace("recovered", "Recovered")
	ok = ok.replace("active", "Active Cases")
	ok = ok.replace("tests", "Tests Taken")
	ok = ok.replace("Tests TakenPerOneMillion", "Tests Taken per One Million People")
	return '<html><head><title>US Statistics</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.min.css"></head><body><center>' + ok + '</center></body></html>'

def get_all():
	yeet = requests.get("https://corona.lmao.ninja/v2/all").content.decode("utf-8")
	ok = json2html.convert(json = yeet)
	ok = ok.replace("state", "State")
	ok = ok.replace("cases", "Cases")
	ok = ok.replace("todayCases", "Cases Today")
	ok = ok.replace("deaths", "Deaths")
	ok = ok.replace("todayDeaths", "Deaths Today")
	ok = ok.replace("recovered", "Recovered")
	ok = ok.replace("active", "Active Cases")
	ok = ok.replace("tests", "Tests Taken")
	ok = ok.replace("Tests TakenPerOneMillion", "Tests Taken per One Million People")
	return '<html><head><title>General Statistics</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.min.css"></head><body><center>' + ok + '</center></body></html>'

def get_world():
	yeet = requests.get("https://corona.lmao.ninja/v2/jhucsse").content.decode("utf-8")
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

app.run(host='0.0.0.0')