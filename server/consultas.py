from flask import Flask
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(host='localhost', database='feelscan', user='postgres', password='j73987927j')
cur = conn.cursor()


# devuelve número de registros
@app.route('/dashboard')
def datos_generales():
    satisfaccion = 'satisfaccion'
    motivacion = 'motivacion'
    felicidad = 'felicidad'
    tristeza = 'tristeza'
    enojo = 'enojo'
    ansiedad = 'ansiedad'
    estres = 'estres'
    aburrimiento = 'aburrimiento'
    alivio = 'alivio'
    frustracion = 'frustracion'
    preocupacion = 'preocupacion'
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (satisfaccion,))
    datos = cur.fetchone()
    nt_satisfaccion = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (motivacion,))
    datos = cur.fetchone()
    nt_motivacion = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (felicidad,))
    datos = cur.fetchone()
    nt_felicidad = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (tristeza,))
    datos = cur.fetchone()
    nt_tristeza = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (enojo,))
    datos = cur.fetchone()
    nt_enojo = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (ansiedad,))
    datos = cur.fetchone()
    nt_ansiedad = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (estres,))
    datos = cur.fetchone()
    nt_estres = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (aburrimiento,))
    datos = cur.fetchone()
    nt_aburrimiento = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (alivio,))
    datos = cur.fetchone()
    nt_alivio = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (frustracion,))
    datos = cur.fetchone()
    nt_frustracion = datos[0]
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (preocupacion,))
    datos = cur.fetchone()
    nt_preocupacion = datos[0]
    cur.execute("SELECT count(*) FROM emociones;")
    datos = cur.fetchone()
    total = datos[0]
    resultado = {"satisfaccion": nt_satisfaccion, "motivacion": nt_motivacion, "felicidad": nt_felicidad,
                 "tristeza": nt_tristeza, "enojo": nt_enojo, "ansiedad": nt_ansiedad, "estres": nt_estres,
                 "aburrimiento": nt_aburrimiento, "alivio": nt_alivio, "frustracion": nt_frustracion,
                 "preocupacion": nt_preocupacion, "total_emociones": total}
    return resultado


# devuelve número de registros
@app.route('/dashboard/<emocion>')
def obtener_cantidad(emocion):
    cur.execute("SELECT count(*) FROM emociones WHERE emocion = %s;", (emocion,))
    datos = cur.fetchone()
    cantidad = datos[0]
    resultado = {"cantidad": cantidad}
    return resultado


# devuelve número de registros
@app.route('/dashboard/<emocion>/<area>')
def obtener_cantidad_por_area(emocion, area):
    cur.execute("""
    SELECT count(*)
    FROM emociones
    WHERE emociones.id IN
    (SELECT miembros.id
    FROM miembros
    WHERE miembros.area = %s)
    AND emociones.emocion = %s
    """, (area, emocion))
    datos = cur.fetchone()
    cantidad = datos[0]
    resultado = {"cantidad": cantidad}
    return resultado


# para devolver personas se debe filtrar id y fechahora
# devuelve número personas en una fecha determinada
@app.route('/dashboard/seleccion_por_fecha/<fecha>/<emocion>')
def obtener_personas_por_fecha(fecha, emocion):
    cur.execute("""
    SELECT DISTINCT emociones.id
    FROM emociones
    WHERE fechahora LIKE %s
    AND emocion = %s
    """, (fecha + 'T%', emocion))
    datos = cur.fetchall()
    personas = len(datos)
    resultado = {"personas_ese_dia": personas}
    return resultado


# devuelve número personas de una área determinada en una fecha determinada
@app.route('/dashboard/seleccion_por_fecha/<fecha>/<emocion>/<area>')
def obtener_personas_por_fecha_y_area(fecha, emocion, area):
    cur.execute("""
    SELECT DISTINCT emociones.id
    FROM emociones
    WHERE emociones.id IN 
    (SELECT miembros.id
    FROM miembros
    WHERE miembros.area = %s)
    AND fechahora LIKE %s
    AND emocion = %s
    """, (area, fecha + 'T%', emocion))
    datos = cur.fetchall()
    personas = len(datos)
    resultado = {"personas_ese_dia": personas}
    return resultado


# devuelve número de personas desde una fecha determinada
@app.route('/dashboard/seleccion_desde_fecha/<fecha_inicial>/<tiempo_inicial>/<fecha_final>/'
           '<tiempo_final>/<emocion>')
def obtener_personas_desde_fecha(fecha_inicial, tiempo_inicial, fecha_final, tiempo_final, emocion):
    cur.execute("""
    SELECT DISTINCT fechahora
    FROM emociones
    WHERE fechahora BETWEEN %s AND %s
    ORDER BY fechahora ASC
    """, (fecha_inicial+'T'+tiempo_inicial, fecha_final+'T'+tiempo_final))
    datos = cur.fetchall()
    fechashoras = []
    for i in range(0, len(datos), 975):
        fechashoras.append(datos[i][0])
    resultado = {}
    for j in fechashoras:
        resultado[j[0:10]] = obtener_personas_por_fecha(j[0:10], emocion)
    return resultado


# devuelve número de personas de un área determinada desde una fecha determinada
@app.route('/dashboard/seleccion_desde_fecha/<fecha_inicial>/<tiempo_inicial>/<fecha_final>/'
           '<tiempo_final>/<emocion>/<area>')
def obtener_personas_desde_fecha_por_area(fecha_inicial, tiempo_inicial, fecha_final, tiempo_final, emocion, area):
    cur.execute("""
    SELECT DISTINCT fechahora
    FROM emociones
    WHERE emociones.id IN 
    (SELECT miembros.id
    FROM miembros
    WHERE miembros.area = %s)
    AND fechahora BETWEEN %s AND %s
    ORDER BY fechahora ASC
    """, (area, fecha_inicial+'T'+tiempo_inicial, fecha_final+'T'+tiempo_final))
    datos = cur.fetchall()
    fechashoras = []
    for i in range(0, len(datos), 975):
        fechashoras.append(datos[i][0])
    resultado = {}
    for j in fechashoras:
        resultado[j[0:10]] = obtener_personas_por_fecha(j[0:10], emocion)
    return resultado


if __name__ == '__main__':
    app.run()
