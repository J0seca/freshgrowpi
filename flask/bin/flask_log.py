#!/usr/bin/python3
# -*- coding: utf8 -*-
import os
import time
import pandas as pd
import numpy as np


def procesa_datos(archivo_log):

    df = pd.read_csv(archivo_log, sep= ";")
    df.columns = ['Fecha','Hora','Temp','Humedad','Vent','Ext','Luz']

    #guardamos variable fecha
    fecha = df['Fecha'][0]
    #eliminamos columnas
    del(df['Fecha'])

    #cambiamos tipo de variables
    df = df.astype({"Vent":'object', "Ext":'object', "Luz":'object',"Humedad":'int64'})
    df = df.astype({"Temp":'object',"Humedad":'object'})

    df['Temp'] = df['Temp'].astype(str) + " °C"
    df['Humedad'] = df['Humedad'].astype(str) + " %"


    #cambiando 1 y 0 por On y Off
    df.loc[df['Vent'] == 1, 'Vent'] = 'On'
    df.loc[df['Vent'] == 0, 'Vent'] = 'Off'
    df.loc[df['Ext'] == 1, 'Ext'] = 'On'
    df.loc[df['Ext'] == 0, 'Ext'] = 'Off'
    df.loc[df['Luz'] == 1, 'Luz'] = 'On'
    df.loc[df['Luz'] == 0, 'Luz'] = 'Off'

    return df


def flask_log():
    archivo_log = "../log/log_clima_" + time.strftime("%d-%m-%y") + ".csv"
    if os.path.isfile(archivo_log) == False:
        #print("Error abriendo archivo LOG")
        df = ['Fecha','Hora','Temp','Humedad','Vent','Ext','Luz1']
        return df

    else:
        variables = procesa_datos(archivo_log)
        return variables

flask_log()
