#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import pandas as pd

def lista_log():
    #listamos archivos de directorio log
    arch_log = os.listdir("/home/pi/freshgrowpi/log/")
    lista_fechas = []

    for i in arch_log:
        i = i[10:18]
        lista_fechas.append(i)
    return lista_fechas

def consulta_log(fecha):
    archivo_log = "/home/pi/freshgrowpi/log/log_clima_" + fecha + ".csv"
    df = pd.read_csv(archivo_log, sep= ";", header=None)
    df.columns = ['Fecha','Hora','Temp','Hum','Vent','Ext','Luz']

    #eliminamos columnas
    del(df['Fecha'])

    #cambiamos tipo de variables
    df = df.astype({"Vent":'object', "Ext":'object', "Luz":'object',"Hum":'int64'})

    df['Temp'] = df['Temp'].astype(str) + "  °C"
    df['Hum'] = df['Hum'].astype(str) + "  %"


    #cambiando 1 y 0 por On y Off
    df.loc[df['Vent'] == 1, 'Vent'] = 'On'
    df.loc[df['Vent'] == 0, 'Vent'] = 'Off'
    df.loc[df['Ext'] == 1, 'Ext'] = 'On'
    df.loc[df['Ext'] == 0, 'Ext'] = 'Off'
    df.loc[df['Luz'] == 1, 'Luz'] = 'On'
    df.loc[df['Luz'] == 0, 'Luz'] = 'Off'

    return df

