#!/usr/bin/python3
# --*-- coding: utf-8 --*--
from scripts.config.variables import vent_temp_max, vent_hum_max, ext_temp_max, ext_hum_max, luz_hora_encendido, luz_hora_apagado, correo_datos, frecuencia_correos
import os
import time

global vent_temp_max, vent_hum_max, ext_temp_max, ext_hum_max, luz_hora_encendido, luz_hora_apagado, correo_datos, frecuencia_correos


#antes que todo:
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
        print("configura_extractor()")
    elif main_option == 3:
        print("configura_fotoperiodo()")
    elif main_option == 4:
        print("configura_correo()")
    elif main_option == 5:
        print("guarda_configuracion()")
    elif main_option == 6:
        clr()
        print("""  __            _                             _
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
    print("-"*25)
    print("Temperatura de encendido actual:", vent_temp_max, "°C")
    print("-"*25)
    nvent_temp_max = input("Ingrese nueva temperatura de encendido: ")
    try:
        nvent_temp_max = int(nvent_temp_max)
        if (1 <= nvent_temp_max < 45):
            ##### ERROR vent_temp_max = nvent_temp_max
            print("Nueva temperatura registrada:", vent_temp_max, "°C")
            time.sleep(2)
            input("Enter para continuar...")
            inicio()
        else:
            print("-"*25)
            print("Datos fuera de Rango. Rango permitido (1 °C a 44 °C)")
            time.sleep(2)
            configura_ventilador()
    except ValueError:
        print("-"*25)
        print("Error ingresando datos.")
        time.sleep(2)
        configura_ventilador()



def main():
    inicio()
main()
