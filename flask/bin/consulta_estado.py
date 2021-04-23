#!/usr/bin/python3
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import sys
#importando datos del archivo de variables
#primero agregamos directorio a los directorios del sistema
sys.path.append('/home/pi/freshgrowpi/scripts/config/')
from variables import *

sensor = Adafruit_DHT.DHT11
pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT) #extractor
GPIO.setup(24,GPIO.OUT) #ventilador
GPIO.setup(21,GPIO.OUT) #luces

def consulta():
    #extractor
    if GPIO.input(25) == 1:
        estado_ext = "on"
    elif GPIO.input(25) == 0:
        estado_ext = "off"
    else:
        estado_ext = "Error"

    #ventilador
    if GPIO.input(24) == 1:
        estado_vent = "on"
    elif GPIO.input(24) == 0:
        estado_vent = "off"
    else:
        estado_vent = "Error"


    #luces
    if GPIO.input(21) == 1:
        estado_luces = "on"
    elif GPIO.input(21) == 0:
        estado_luces = "off"
    else:
        estado_luces = "Error"

    try:
        hum, temp = Adafruit_DHT.read_retry(sensor, pin)
        temp_actual = str(temp)[0:2]
        hum_actual = str(hum)[0:2]
        hora_actual = time.strftime("%H:%M")
    except:
        temp_actual = "Error"
        hum_actual = "Error"
        hora_actual = "Error"
    return estado_ext, estado_vent, estado_luces, temp_actual, hum_actual, hora_actual, correo_datos, vent_temp_max, vent_hum_max, ext_temp_max, ext_hum_max, luz_hora_encendido, luz_hora_apagado, correo_datos, frecuencia_correos

#print(consulta())
