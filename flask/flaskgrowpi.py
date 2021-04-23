#!/usr/bin/python3
from flask import Flask as F
from flask import render_template
from bin.flask_log import *
from bin.flask_reporte import *
from bin.consulta_estado import *
from bin.flask_control import *

app = F(__name__)

@app.route('/')
def flaskgrowpi():
    return render_template('index.html')

@app.route('/reporte')
def reporte_web():
    datos_reporte = reporte()
    return render_template('reporte.html',
                                temp_min=datos_reporte[0], 
                                temp_max=datos_reporte[1],
                                temp_prom=datos_reporte[2], 
                                hum_min=datos_reporte[3],
                                hum_max=datos_reporte[4],
                                hum_prom=datos_reporte[5],
                                prop_vent=datos_reporte[6],
                                prop_ext=datos_reporte[7])

estilo_tabla="""
<style type="text/css" media="screen">
    table.tablalog {
      font-family: "Trebuchet MS", Arial;
      font-size: 1em;
      background: #6F9D76;
      border-collapse: collapse;
      text-align: left;
      border: 2px solid purple;
      width: 100%;
      }
      th {
      color: #68D21A;
      background-color: #64006C;
      }
      td {
      color: #64006C;
      }
}
    </style>
"""

@app.route('/log')
def log():
    fecha = time.strftime("%d-%m-%y")
    datos_log = flask_log()
    try:
        datos = estilo_tabla + datos_log.to_html(index=False).replace("dataframe", "tablalog")
    except:
        datos = estilo_tabla + """
<table border="1" class="tablalog">
  <thead>
    <tr style="text-align: right;">
      <th>Hora</th>
      <th>Temp</th>
      <th>Hum</th>
      <th>Vent</th>
      <th>Ext</th>
      <th>Luz</th>
    </tr>
  </thead>"""
    return render_template('log.html', fecha=fecha, datos_log=datos)

@app.route('/control')
def control():
    datos_actualizados = consulta()
    return render_template('control.html', estado_ext=datos_actualizados[0],
                                            estado_vent=datos_actualizados[1],
                                            estado_luces=datos_actualizados[2],
                                            temp_actual=datos_actualizados[3],
                                            hum_actual=datos_actualizados[4],
                                            hora_actual=datos_actualizados[5],
                                            vent_temp_max=datos_actualizados[7],
                                            vent_hum_max=datos_actualizados[8],
                                            ext_temp_max=datos_actualizados[9],
                                            ext_hum_max=datos_actualizados[10],
                                            luz_hora_encendido=datos_actualizados[11],
                                            luz_hora_apagado=datos_actualizados[12])

@app.route('/vent_on')
def vent_on():
    prende_ventilador()
    datos_actualizados = consulta()
    return render_template('control.html', estado_ext=datos_actualizados[0],
                                            estado_vent=datos_actualizados[1],
                                            estado_luces=datos_actualizados[2],
                                            temp_actual=datos_actualizados[3],
                                            hum_actual=datos_actualizados[4],
                                            hora_actual=datos_actualizados[5],
                                            vent_temp_max=datos_actualizados[7],
                                            vent_hum_max=datos_actualizados[8],
                                            ext_temp_max=datos_actualizados[9],
                                            ext_hum_max=datos_actualizados[10],
                                            luz_hora_encendido=datos_actualizados[11],
                                            luz_hora_apagado=datos_actualizados[12])


@app.route('/vent_off')
def vent_off():
    apaga_ventilador()
    datos_actualizados = consulta()
    return render_template('control.html', estado_ext=datos_actualizados[0],
                                            estado_vent=datos_actualizados[1],
                                            estado_luces=datos_actualizados[2],
                                            temp_actual=datos_actualizados[3],
                                            hum_actual=datos_actualizados[4],
                                            hora_actual=datos_actualizados[5],
                                            vent_temp_max=datos_actualizados[7],
                                            vent_hum_max=datos_actualizados[8],
                                            ext_temp_max=datos_actualizados[9],
                                            ext_hum_max=datos_actualizados[10],
                                            luz_hora_encendido=datos_actualizados[11],
                                            luz_hora_apagado=datos_actualizados[12])


@app.route('/ext_on')
def ext_on():
    prende_extractor()
    datos_actualizados = consulta()
    return render_template('control.html', estado_ext=datos_actualizados[0],
                                            estado_vent=datos_actualizados[1],
                                            estado_luces=datos_actualizados[2],
                                            temp_actual=datos_actualizados[3],
                                            hum_actual=datos_actualizados[4],
                                            hora_actual=datos_actualizados[5],
                                            vent_temp_max=datos_actualizados[7],
                                            vent_hum_max=datos_actualizados[8],
                                            ext_temp_max=datos_actualizados[9],
                                            ext_hum_max=datos_actualizados[10],
                                            luz_hora_encendido=datos_actualizados[11],
                                            luz_hora_apagado=datos_actualizados[12])


@app.route('/ext_off')
def ext_off():
    apaga_extractor()
    datos_actualizados = consulta()
    return render_template('control.html', estado_ext=datos_actualizados[0],
                                            estado_vent=datos_actualizados[1],
                                            estado_luces=datos_actualizados[2],
                                            temp_actual=datos_actualizados[3],
                                            hum_actual=datos_actualizados[4],
                                            hora_actual=datos_actualizados[5],
                                            vent_temp_max=datos_actualizados[7],
                                            vent_hum_max=datos_actualizados[8],
                                            ext_temp_max=datos_actualizados[9],
                                            ext_hum_max=datos_actualizados[10],
                                            luz_hora_encendido=datos_actualizados[11],
                                            luz_hora_apagado=datos_actualizados[12])

@app.route('/luces_on')
def luces_on():
    prende_luces()
    datos_actualizados = consulta()
    return render_template('control.html', estado_ext=datos_actualizados[0],
                                            estado_vent=datos_actualizados[1],
                                            estado_luces=datos_actualizados[2],
                                            temp_actual=datos_actualizados[3],
                                            hum_actual=datos_actualizados[4],
                                            hora_actual=datos_actualizados[5],
                                            vent_temp_max=datos_actualizados[7],
                                            vent_hum_max=datos_actualizados[8],
                                            ext_temp_max=datos_actualizados[9],
                                            ext_hum_max=datos_actualizados[10],
                                            luz_hora_encendido=datos_actualizados[11],
                                            luz_hora_apagado=datos_actualizados[12])


@app.route('/luces_off')
def luces_off():
    apaga_luces()
    datos_actualizados = consulta()
    return render_template('control.html', estado_ext=datos_actualizados[0],
                                            estado_vent=datos_actualizados[1],
                                            estado_luces=datos_actualizados[2],
                                            temp_actual=datos_actualizados[3],
                                            hum_actual=datos_actualizados[4],
                                            hora_actual=datos_actualizados[5],
                                            vent_temp_max=datos_actualizados[7],
                                            vent_hum_max=datos_actualizados[8],
                                            ext_temp_max=datos_actualizados[9],
                                            ext_hum_max=datos_actualizados[10],
                                            luz_hora_encendido=datos_actualizados[11],
                                            luz_hora_apagado=datos_actualizados[12])


if __name__ == '__main__':
    app.run(host='192.168.0.13', port=8888, debug=True)
