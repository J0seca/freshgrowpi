#!/usr/bin/python3
#-*- coding: utf-8 -*-
#Automatiza extractores adicionales.
#Extractores se prenden cuando
#se supera cierta temperatura o humedad
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
from config.variables import ext_temp_max, ext_hum_max

#configurando GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

#variables de sensor
sensor = Adafruit_DHT.DHT11
pin = 4
temp_max = int(ext_temp_max)
hum_max = int(ext_hum_max)

#funciones de encendido/apagado 1/0
def prende_extractor():
    GPIO.output(25, True)
    #print(GPIO.input(25))

def apaga_extractor():
    GPIO.output(25, False)
    #print(GPIO.input(25))

def main():
    while True:
        hum, temp = Adafruit_DHT.read_retry(sensor, pin)
        temp = str(temp)[0:2]
        hum = str(hum)[0:1]
        print(temp, hum, temp_max, hum_max)

        if (int(temp) >= temp_max) or (int(hum) >= hum_max) and (int(GPIO.input(25)) == 0):
            print("Temp/Hum muy alta. Prendiendo extractores.")
            prende_extractor()
            time.sleep(36000) #extractores encendidos por 10 min.
            print("Apagando extractores.")
            apaga_extractor()

        else:
            if GPIO.input(25) == 1:
                print("Parámetros correctos. Apagando extractor.")
                apaga_extractor()

        print("Descansando un minuto u.u")
        time.sleep(60)

main()
