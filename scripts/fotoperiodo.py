#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import time
import datetime

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

hora_encendido = luz_hora_encendido
hora_apagado = luz_hora_apagado
hora_encendido = datetime.datetime.strptime(hora_encendido, '%H:%M')
hora_apagado = datetime.datetime.strptime(hora_apagado, '%H:%M')

#haciendo rango de horas de día en minutos segun rango:
rango_encendido = []
hora = hora_encendido
while hora != hora_apagado:
    #agregamos hora a lista de rango:
    rango_encendido.append(hora)
    #print(hora)

    #sumamos un minuto:
    hora = hora + datetime.timedelta(minutes=1)

    #aca buscamos el limite del otro día, ya que el horario puede pasar las 00:00
    #por lo que se reinicia a las 00:00 del día 1
    limite = "00:00"
    limite = datetime.datetime.strptime(limite, '%H:%M') +datetime.timedelta(days=1)

    if hora == limite:
        hora = "00:00" #reseteamos a día 1
        hora = datetime.datetime.strptime(hora, '%H:%M') #aplicamos formato
    #time.sleep(0.2)

#verificando luces prendidas
while True:
    hora_consulta = datetime.datetime.now().strftime("%H:%M")
    hora_consulta = datetime.datetime.strptime(hora_consulta, '%H:%M')
    if hora_consulta in rango_encendido:
        if (GPIO.input(21) == 0):
            comienza_dia()
        else:
            print("Estado de luces correcto.")
    else:
        if (GPIO.input(21) == 1):
            comienza_noche()
        else:
            print("Estado de luces correcto.")

    time.sleep(58)
