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
temp_max = vent_temp_max
hum_max = vent_hum_max

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
        head = "Temp:", temp, "Hum:", hum, "Temp max:", temp_max, "Hum max:", hum_max
        print(head)
        estado_v = GPIO.input(24)
        print("estado de ventilador:", estado_v)

        try:
            if int(temp) >= temp_max  and int(estado_v) == 0:
                print("Temperatura muy alta. Prendiendo ventiladores.")
                prende_ventilador()
                time.sleep(600) #ventiladores encendidos por 10 min.
                print("Apagando ventiladores.")
                apaga_ventilador()

            elif int(hum) >= hum_max and int(estado_v) == 0:
                print("Humedad muy alta. Prendiendo ventiladores.")
                prende_ventilador()
                time.sleep(600) #ventiladores encendidos por 10 min.
                print("Apagando ventiladores.")
                apaga_ventilador()

            else:
                print("Parámetros correctos. Apagando ventilador.")

        except:
            print("Error de datos")


        apaga_ventilador()
        print("Descansando")
        time.sleep(30)
main()
