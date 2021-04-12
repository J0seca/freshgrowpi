#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import time
import RPi.GPIO as GPIO
from config.variables import luz_hora_encendido, luz_hora_apagado

#configurando GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
#GPIO.input(21)

def comienza_dia():
    GPIO.output(21, True)
    print("Comenzando el día!, Luces ON!", GPIO.input(21))

def comienza_noche():
    GPIO.output(21, False)
    print("Terminando el día. Buenas noches", GPIO.input(21))

print("Encendiendo a las: ", luz_hora_encendido)
print("Apagando a las: ", luz_hora_apagado)

while True:

    hora_actual = int(time.strftime("%H"))
    minuto_actual = int(time.strftime("%M"))
    hora_encendido = int(luz_hora_encendido[0:2])
    minuto_encendido = int(luz_hora_encendido[3:5])
    hora_apagado = int(luz_hora_apagado[0:2])
    minuto_apagado = int(luz_hora_apagado[3:5])

    print("Hora actual:", hora_actual)
    print("Minuto actual:", minuto_actual)
    print("Hora encendido:", hora_encendido)
    print("Minuto encendido:", minuto_encendido)
    print("Hora apagado:", hora_apagado)
    print("Minuto apagado:", minuto_apagado)

    if (hora_actual == hora_encendido) and (minuto_actual == minuto_encendido) and (GPIO.input(21) == 0):
        comienza_dia()

    if (hora_actual == hora_apagado) and (minuto_actual == minuto_apagado) and (GPIO.input(21) == 1):
        comienza_noche()

    else:
        print("Luces en estado correcto:", GPIO.input(21))
    time.sleep(30)
