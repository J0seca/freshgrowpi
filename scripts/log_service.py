#!/usr/bin/python3
# -*- coding: utf8 -*-
import os
import time
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 4
sleep = 6 #duerme en segundos 1800 para media hora
logfile = "../log/log_clima_" + time.strftime("%d-%m-%y") + ".csv"

while True:
    try:
        hum, temp = Adafruit_DHT.read_retry(sensor, pin)
        temp = str(temp)[0:2]
        hum = str(hum)[0:2]
        fecha = time.strftime("%d-%m-%y")
        hora = time.strftime("%H:%M")
        log_data = fecha + ";" + hora + ";" + temp + ";" + hum
        #print(log_data)

    except ValueError:
        temp = "error"
        hum = "error"
        fecha = time.strftime("%d-%m-%y")
        hora = time.strftime("%H:%M")
        log_data = fecha + ";" + hora + ";" + temp + ";" + hum

    if os.path.isfile(logfile):
        print("Archivo encontrado: ", logfile, " Escribiendo datos.")
        _log = open(logfile, "r")
        _log_lines = _log.readlines()
        #_log_lines.append(log_data)
        _log.close()
        _log = open(logfile, "w")
        for line in _log_lines:
            #print("Escribiendo:", line)
            line = line.strip("\n")
            _log.write(line + "\n")
        _log.write(log_data)
        _log.close()

    else:
        print("Archivo de registro no existe. Creando nuevo archivo CSV.")
        _log = open(logfile, "w")
        print("Archivo creado. Escribiendo datos...")
        _log.write(log_data)
        _log.close()
    time.sleep(sleep)
