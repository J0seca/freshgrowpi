from flask import Flask as F
from flask import render_template
from bin.flask_log import *
from bin.flask_reporte import *

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
    datos = estilo_tabla + datos_log.to_html(index=False).replace("dataframe", "tablalog")
    return render_template('log.html', fecha=fecha, datos_log=datos)
