#!/usr/bin/python3
#-*- coding: utf-8 -*-
#Automatiza ventiladores adicionales.
#Ventiladores se prenden cuando
#se supera cierta temperatura o humedad
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
from config.variables import vent_temp_max, vent_hum_max

#configurando GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

#variables de sensor
sensor = Adafruit_DHT.DHT11
pin = 4
temp_max = int(vent_temp_max)
hum_max = int(vent_hum_max)

#funciones de encendido/apagado 1/0
def prende_ventilador():
    GPIO.output(24, True)
    #print(GPIO.input(24))

def apaga_ventilador():
    GPIO.output(24, False)
    #print(GPIO.input(24))

def main():
    while True:
        hum, temp = Adafruit_DHT.read_retry(sensor, pin)
        temp = str(temp)[0:2]
        hum = str(hum)[0:1]
        print(temp, hum, temp_max, hum_max)

        if (int(temp) >= temp_max) or (int(hum) >= hum_max) and (int(GPIO.input(24)) == 0):
            print("Temp/Hum muy alta. Prendiendo ventiladores.")
            prende_ventilador()
            time.sleep(36000) #ventiladores encendidos por 10 min.
            print("Apagando ventiladores.")
            apaga_ventilador()

        else:
            if GPIO.input(24) == 1:
                print("Parámetros correctos. Apagando ventilador.")
                apaga_ventilador()

        print("Descansando un minuto u.u")
        time.sleep(60)

main()
