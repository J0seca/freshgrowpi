#!/usr/bin/python3
#-*- coding: utf-8 -*-

import smtplib
import time
import pandas as pd
#from email.mime.text import MIMEText
#from email.mime.multipart import MiMEMultipart
from config.variables import correo_datos, frecuencia_correos

horas_espera = int(frecuencia_correos) * 3600

smtp_server= 'smtp.gmail.com'
port = 587 #465
smtp_user = 'freshgrowpi@gmail.com'
smtp_pass = '1pw0rghs3rf#'

html="""
<style>h1.p{color: blue;}</style>
<h1 class="p">
Informe clima
</h1>
"""
fecha = time.strftime("%d-%m-%y")

text = fecha + """
Datos del día:
"""

mensaje = text
#mensaje = MIMEText(mensaje, "html")
#mensaje = MIMEMultipart()
#mensaje["Subjet"] = "Control clima"

s = smtplib.SMTP(smtp_server + ":" + str(port))
s.starttls()
s.login(smtp_user,smtp_pass)
s.sendmail(smtp_user, correo_datos, mensaje)
s.quit()

print('Correo enviado.')
