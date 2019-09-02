import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledOne = 13
ledTwo =19

ledOne_status = 0
ledTwo_status = 0

GPIO.setup(ledOne, GPIO.OUT)
GPIO.setup(ledTwo, GPIO.OUT)

GPIO.output(ledOne, GPIO.LOW)
GPIO.setup(ledTwo, GPIO.OUT)

@app.route('/')
def index():
    ledOne_status = GPIO.input(ledOne)
    ledTwo_status = GPIO.input(ledTwo)
   
    statusData = { 'ledOne' : ledOne_status,'ledTwo' : ledTwo_status}
   
    return render_template('index.html', **statusData)

@app.route('/<deviceName>/<action>')
def controlDevices(deviceName, action):
    if deviceName == "ledOne":
        device = ledOne
    if deviceName == "ledTwo":
        device = ledTwo


    if action == "On":
        GPIO.output(device, GPIO.HIGH)
    if action == "off":
        GPIO.output(device, GPIO.LOW)

    ledOne_status = GPIO.input(ledOne)
    ledTwo_status = GPIO.input(ledTwo)

    statusData = { 'ledOne' : ledOne_status,'ledTwo' : ledTwo_status}

    return render_template('index.html', **statusData)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)