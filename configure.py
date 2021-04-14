#!/usr/bin/python3
# --*-- coding: utf-8 --*--
from scripts.config.variables import vent_temp_max, vent_hum_max, ext_temp_max, ext_hum_max, luz_hora_encendido, luz_hora_apagado, correo_datos, frecuencia_correos
import os
import time

#variables globales
global vent_temp_max, vent_hum_max, ext_temp_max, ext_hum_max, luz_hora_encendido, luz_hora_apagado, correo_datos, frecuencia_correos
global nvent_temp_max, vent_hum_max, next_temp_max, ext_hum_max, nluz_hora_encendido, nluz_hora_apagado, ncorreo_datos, nfrecuencia_correos

#definimos nuevas
nvent_temp_max = vent_temp_max
nvent_hum_max = vent_hum_max
next_temp_max = ext_temp_max
next_hum_max = ext_hum_max
nluz_hora_encendido = luz_hora_encendido
nluz_hora_apagado = luz_hora_apagado
ncorreo_datos = correo_datos
nfrecuencia_correos = frecuencia_correos

#primero que todo:
def clr():
    os.system("clear")

def inicio():
    clr()
    print("""
    ---------------------*---------------------
     ___           _    ___                ___ _
    | __| _ ___ __| |_ / __|_ _ _____ __ _| _ (_)
    | _| '_/ -_|_-< ' \ (_ | '_/ _ \ V  V /  _/ |
    |_||_| \___/__/_||_\___|_| \___/\_/\_/|_| |_|

    ---------------------*---------------------

     Configuración:


    1- Humedad y temperatura máxima ventilador.

    2- Humedad y temperatura máxima extractor.

    3- Fotoperiodo.

    4- Notificación por correo electrónico.

    5- Guardar nueva configuración.

    6- Salir.
    """)
    main_option = input("Ingrese opción: ")

    #verificando si se ingresó una opción correcta:
    try:
        main_option = int(main_option)
    except ValueError:
        print("\n\n Opción incorrecta!")
        time.sleep(1)
        inicio()

    if main_option == 1:
        configura_ventilador()
    elif main_option == 2:
        configura_extractor()
    elif main_option == 3:
        configura_fotoperiodo()
    elif main_option == 4:
        configura_correo()
    elif main_option == 5:
        print("guarda_configuracion()")
    elif main_option == 6:
        clr()
        print("""
      __            _                             _
     / _|_ _ ___ __| |_  __ _ _ _ _____ __ ___ __(_)
    |  _| '_/ -_|_-< ' \/ _` | '_/ _ \ V  V / '_ \ |
    |_| |_| \___/__/_||_\__, |_| \___/\_/\_/| .__/_|
                        |___/               |_|

Saliendo del programa! """)
        time.sleep(1)
        exit()
    else:
        print("\n\n Opción incorrecta!*" , main_option)
        time.sleep(1)
        inicio()



def configura_ventilador():
    clr()
    print("""
                 _   _ _         _
    __ _____ _ _| |_(_) |__ _ __| |___ _ _
    \ V / -_) ' \  _| | / _` / _` / _ \ '_|
     \_/\___|_||_\__|_|_\__,_\__,_\___/_|

    """)
    #Configurando tempreratura:

    print("-"*25)
    print("Temperatura de encendido actual:", vent_temp_max, "°C")
    print("-"*25)
    global nvent_temp_max
    nvent_temp_max = input("Ingrese nueva temperatura de encendido: ")

    try:
        nvent_temp_max = int(nvent_temp_max)
        if (1 <= nvent_temp_max < 45):
            ##### ERROR vent_temp_max = nvent_temp_max
            print("Nueva temperatura registrada:", nvent_temp_max, "°C\n")
            time.sleep(2)
            #input("Enter para continuar...\n\n")
            #inicio()
        else:
            print("-"*25)
            print("Datos fuera de Rango. Rango permitido (1 °C a 44 °C)")
            time.sleep(3)
            configura_ventilador()

    except ValueError:
        print("-"*25)
        print("Error ingresando datos.")
        time.sleep(2)
        configura_ventilador()

    #Configurando humedad:

    print("-"*25)
    print("Humedad de encendido actual:", vent_hum_max, "%")
    print("-"*25)
    global nvent_hum_max
    nvent_hum_max = input("Ingrese nueva humedad de encendido: ")
    try:
        nvent_hum_max = int(nvent_hum_max)
        if (1 <= nvent_hum_max < 99):
            print("Nueva humedad registrada:", nvent_hum_max, "%")
            time.sleep(2)
            input("\nEnter para continuar...")
            inicio()
        else:
            print("-"*25)
            print("Datos fuera de Rango. Rango permitido (1% a 99%)")
            time.sleep(3)
            configura_ventilador()
    except ValueError:
        print("-"*25)
        print("Error ingresando datos.")
        time.sleep(2)
        configura_ventilador()

    return nvent_temp_max, nvent_hum_max

def configura_extractor():
    clr()
    print("""
             _               _
     _____ _| |_ _ _ __ _ __| |_ ___ _ _
    / -_) \ /  _| '_/ _` / _|  _/ _ \ '_|
    \___/_\_\\__|_| \__,_\__|\__\___/_|

    """)
    #Configurando tempreratura:

    print("-"*25)
    print("Temperatura de encendido actual:", ext_temp_max, "°C")
    print("-"*25)
    global next_temp_max
    next_temp_max = input("Ingrese nueva temperatura de encendido: ")

    try:
        next_temp_max = int(next_temp_max)
        if (1 <= next_temp_max < 45):
            print("Nueva temperatura registrada:", next_temp_max, "°C\n")
            time.sleep(2)
            #input("Enter para continuar...\n\n")
        else:
            print("-"*25)
            print("Datos fuera de Rango. Rango permitido (1 °C a 44 °C)")
            time.sleep(3)
            configura_extractor()

    except ValueError:
        print("-"*25)
        print("Error ingresando datos.")
        time.sleep(2)
        configura_extractor()

    #Configurando humedad:

    print("-"*25)
    print("Humedad de encendido actual:", ext_hum_max, "%")
    print("-"*25)
    global next_hum_max
    next_hum_max = input("Ingrese nueva humedad de encendido: ")
    try:
        next_hum_max = int(next_hum_max)
        if (1 <= next_hum_max < 99):
            print("Nueva humedad registrada:", next_hum_max, "%")
            time.sleep(2)
            input("\nEnter para continuar...")
            inicio()
        else:
            print("-"*25)
            print("Datos fuera de Rango. Rango permitido (1% a 99%)")
            time.sleep(3)
            configura_extractor()
    except ValueError:
        print("-"*25)
        print("Error ingresando datos.")
        time.sleep(2)
        configura_extractor()

    return next_temp_max, next_hum_max


def configura_fotoperiodo():
    clr()
    print("""
      __     _                     _         _
     / _|___| |_ ___ _ __  ___ _ _(_)___  __| |___
    |  _/ _ \  _/ _ \ '_ \/ -_) '_| / _ \/ _` / _ \\
    |_| \___/\__\___/ .__/\___|_| |_\___/\__,_\___/
                    |_|
    """)

    global nluz_hora_encendido
    print("-"*25)
    print("Hora de encendido registrada:", luz_hora_encendido)
    print("-"*25)
    nluz_hora_encendido = input("Ingrese nueva hora de encendido: ")

    #verificamos formato:
    try:
        hora = int(nluz_hora_encendido[0:2])
        minuto = int(nluz_hora_encendido[3:5])
        sep = nluz_hora_encendido[2]

        if(0 <= hora <= 23) and (0 <= minuto <= 59) and (sep == ":") and (len(nluz_hora_encendido) == 5):
            print("\nRegistrando nueva hora de endendido:", nluz_hora_encendido)
            time.sleep(3)
            #inicio()
        else:
            print("\nError de formato!, Ejemplo:  01:34")
            time.sleep(3)
            configura_fotoperiodo()

    except ValueError:
        print("\nError de formato!, Ejemplo:  01:34")
        time.sleep(3)
        configura_fotoperiodo()

    global nluz_hora_apagado
    print("-"*25)
    print("Hora de apagado registrada:", luz_hora_apagado)
    print("-"*25)
    nluz_hora_apagado = input("Ingrese nueva hora de apagado: ")

    #verificamos formato:
    try:
        hora = int(nluz_hora_apagado[0:2])
        minuto = int(nluz_hora_apagado[3:5])
        sep = nluz_hora_apagado[2]

        if(0 <= hora <= 23) and (0 <= minuto <= 59) and (sep == ":") and (len(nluz_hora_apagado) == 5):
            print("\nRegistrando nueva hora de apagado:", nluz_hora_apagado)
            time.sleep(3)
            input("\nEnter para continuar...")
            inicio()

        else:
            print("\nError de formato!, Ejemplo:  01:34")
            time.sleep(3)
            configura_fotoperiodo()

    except ValueError:
        print("\nError de formato!, Ejemplo:  01:34")
        time.sleep(3)
        configura_fotoperiodo()

    return nluz_hora_encendido, nluz_hora_apagado

def configura_correo():
    print("Nueva hora de encendido:", nluz_hora_encendido, "\nNueva hora apagado:", nluz_hora_apagado)


def main():
    inicio()
main()
