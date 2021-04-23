#-*- coding: utf-8 -*-
#controla dispositivos desde flask
import RPi.GPIO as GPIO

#configurando GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#funciones de encendido/apagado 1/0
def prende_ventilador():
    GPIO.output(24, True)

def apaga_ventilador():
    GPIO.output(24, False)

def prende_extractor():
    GPIO.output(25, True)

def apaga_extractor():
    GPIO.output(25, False)

def prende_luces():
    GPIO.output(21, True)

def apaga_luces():
    GPIO.output(21, False)
