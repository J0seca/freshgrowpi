#!/usr/bin/python3
# -*- coding: utf8 -*-
import os
import time
import pandas as pd
import numpy as np


def procesa_datos(archivo_log):

    df = pd.read_csv(archivo_log, sep= ";")
    df.columns = ['Fecha','Hora','Temperatura','Humedad','Ventilador','Extractor','Luz']

    #guardamos variable fecha
    fecha = df['Fecha'][0]
    #eliminamos columnas
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

    return df


def main():
    archivo_log = "../log/log_clima_" + time.strftime("%d-%m-%y") + ".csv"

    if os.path.isfile(archivo_log) == False:
        #print("Error abriendo archivo LOG")
        df = ['Fecha','Hora','Temperatura','Humedad','Ventilador','Extractor','Luz']
        return df

    else:
        variables = procesa_datos(archivo_log)
        return variables

main()
