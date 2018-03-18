#!/usr/bin/python
import RPi.GPIO as GPIO
import microgear.client as microgear
import logging
import random
from time import sleep

appid = 'SobmoeiSmartFarm'
gearkey = 'tqI6uEdjYRWfAIC'
gearsecret = 'UpiK0L2RK2bjfnnz3lk2WHQEX'

microgear.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
    logging.info("Now I am connected with netpie")

def subscription(topic,message):
    logging.info(topic+" "+message)

def disconnect():
    logging.debug("disconnect is work")

microgear.setalias("doraemon")
microgear.on_connect = connection
microgear.on_message = subscription
microgear.on_disconnect = disconnect
microgear.subscribe("/mails")
microgear.connect(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)

pump_state = 0

while True:
    if GPIO.input(17) == 1:
            # turn leds on
            print "pump on"
            GPIO.output(4,GPIO.LOW)
            pump_state = 1

            sleep(2) # sleep 1 second

    else:
            # turn leds off
            print "pump off"
            GPIO.output(4,GPIO.HIGH)
            pump_state = 0
            sleep(2) # sleep 1 second
    if (microgear.connected):
            microgear.chat("sensorstatus",str(int(pump_state)))
            data = {"pump":pump_state*10}
            #data = {"field1":random.randint(1, 10),"field2":random.randint(1, 10),"field3":random.randint(1, 10)}
            microgear.writeFeed("sobmeoi",data)

