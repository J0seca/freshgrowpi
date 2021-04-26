#!/usr/bin/python3
# -*- coding: utf8 -*-
import os
import time
import pandas as pd
import numpy as np


def procesa_datos(archivo_log):

    df = pd.read_csv(archivo_log, sep= ";", header=None)
    df.columns= ['Fecha','Hora','Temperatura','Humedad','Ventilador','Extractor','Luz']

    #guardamos variable fecha
    del(df['Fecha'])

    #cambiamos tipo de variables
    df = df.astype({"Ventilador":'object', "Extractor":'object', "Luz":'object'})


    #cambiando 1 y 0 por On y Off
    df.loc[df['Ventilador'] == 1, 'Ventilador'] = 'On'
    df.loc[df['Ventilador'] == 0, 'Ventilador'] = 'Off'
    df.loc[df['Extractor'] == 1, 'Extractor'] = 'On'
    df.loc[df['Extractor'] == 0, 'Extractor'] = 'Off'
    df.loc[df['Luz'] == 1, 'Luz'] = 'On'
    df.loc[df['Luz'] == 0, 'Luz'] = 'Off'

    temp_min = np.amin(df['Temperatura'])
    temp_max = np.amax(df['Temperatura'])
    temp_media = int(round(np.mean(df['Temperatura']), 1))

    hum_min = int(np.amin(df['Humedad']))
    hum_max = int(np.amax(df['Humedad']))
    hum_media = int(round(np.mean(df['Humedad']), 1))

    if len(df) > 2:
        prop_vent = int(round( (len(df.loc[ df['Ventilador'] == "On"]) / len(df) * 100) , 1))
        prop_ext = int(round( (len(df.loc[ df['Extractor'] == "On"]) / len(df) * 100) , 1))
    else:
        prop_vent = "-"
        prop_ext = "-"

    return temp_min, temp_max, temp_media, hum_min, hum_max, hum_media, prop_vent, prop_ext



def reporte():
    archivo_log = "/home/pi/freshgrowpi/log/log_clima_" + time.strftime("%d-%m-%y") + ".csv"

    if os.path.isfile(archivo_log) == False:
        #print("Error abriendo archivo LOG")
        temp_max = "0"
        temp_min = "0"
        temp_media = "0"
        hum_max = "0"
        hum_min = "0"
        hum_media = "0"
        prop_vent = "0"
        prop_ext = "0"

        return temp_min, temp_max, temp_media, hum_min, hum_max, hum_media, prop_vent, prop_ext

    else:
        variables = procesa_datos(archivo_log)
        return variables
#reporte()
