from database import dynamodb as db
from datetime import datetime, timedelta
from collections import Counter
from collections import defaultdict
import ast

def getEmotionPoints(dynamodb = db,tenant_id = 'UTEC'):
    table_name = 't_emociones'
    # Realiza una consulta a la tabla
    response = dynamodb.scan(TableName=table_name)

    # Procesa los resultados
    emociones = {}
    for item in response['Items']:
        if(item['tenant_id']['S'] == tenant_id):
            nombre_emocion = item['nombre']['S']
            valor = item['valor']['N']
            emociones[nombre_emocion] = int(valor)
    return emociones         
       

def getAreas(dynamodb = db,tenant_id = 'UTEC'):
    table_name = 't_areas'
    # Realiza una consulta a la tabla
    response = dynamodb.scan(TableName=table_name)

    # Procesa los resultados
    areas = []
    for item in response['Items']:
        if(item['tenant_id']['S'] == tenant_id):
            nombre_area = item['nombre']['S']
            areas.append(nombre_area)
    return areas


def getHorarios(dynamodb = db,tenant_id ='UTEC'):
    table_name = 't_horario_psicologos'
    # Realiza una consulta a la tabla
    response = dynamodb.scan(TableName=table_name)
    # Procesa los resultados
    horarios = {}
    for item in response['Items']:
        if(item['tenant_id']['S'] == tenant_id):
            codigo = item['code']['S']
            valor = item['horario']['S']
            valor = valor.replace("'", "\"")

            # Analizar el string como una lista de diccionarios
            data = ast.literal_eval(valor)

            # Crear un diccionario con los días como claves y las horas como valores
            horario = {item["dia"]: item["horas"] for item in data}
            days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
            for day in days:
                if day not in horario.keys():
                    horario[day] = []
            horarios[codigo] = horario

    for id in horarios.keys():
        data_member = getMember(id)
        horarios[id]['nombre'] = data_member['nombre']
        horarios[id]['correo'] = data_member['correo']

    return horarios 

#programar para ejecutar cada cierto tiempo de manera interna (lambda con actualizar puntaje)
def calculatePuntaje(dynamodb = db,tenant_id = 'UTEC'):
    table_name = 't_registro_emociones'
    emociones = getEmotionPoints(dynamodb,tenant_id)
    puntajes = {}

    response = dynamodb.scan(TableName=table_name)

    for item in response['Items']:
        if(item['tenant_id']['S'] == tenant_id):
            code = item['code']['S']

            emocion = item['emocion']['S']  
            puntaje_emocion = emociones.get(emocion, 0)

            if code in puntajes:
                puntajes[code] += int(puntaje_emocion)
            else:
                puntajes[code] = int(puntaje_emocion)
    return puntajes


# Lógica para calcular el nuevo score en base al state (cantidad de checkboxs marcados)
def calculateNewScore(actual_score, state):
    if (state == 1):
        return actual_score - 20
    elif (state == 2):
        return actual_score - 50
    elif (state == 3):
        return actual_score - 100


# No es óptimo recorrer todo la tabla para determinar el puntaje, solo debemos modificar el campo puntaje
# en base al valor de estado. El valor de estando va de 1 a 3 y es un input que se da desde el frontend 
def determinarPuntaje(dynamodb = db,tenant_id = 'UTEC'): #corregir debe sumar dado la ultima consulta, por ahora solo actualiza
    table_name = 't_miembros'
    puntaje_a_actualizar = calculatePuntaje(dynamodb,tenant_id)
    for cod, nuevo_puntaje in puntaje_a_actualizar.items():
        # Define la expresión de actualización
        update_expression = "SET puntaje = :val"

        # Define los valores para la expresión de actualización
        expression_attribute_values = {
            ':val': {'N': str(nuevo_puntaje)}  # DynamoDB espera valores en un formato específico
        }

        # Realiza la actualización para cada ID
        response = dynamodb.update_item(
            TableName=table_name,
            Key={'tenant_id': {'S': tenant_id}, 'code': {'S': cod}},  # Especifica la clave primaria para identificar el elemento
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        print(response)

def getEmocionPredominante(dynamodb = db,tenant_id = 'UTEC'):
    fecha_limite = datetime(2023, 8, 28, 0, 0, 0)

    items = getDataTiempo(dynamodb, tenant_id, fecha_limite)

    # Extrae las emociones en una lista
    emociones = [item['emocion']['S'] for item in items]

    # Cuenta las ocurrencias de cada emoción
    contador_emociones = Counter(emociones)

    # Encuentra la emoción más común
    emocion_mas_comun = contador_emociones.most_common(1)[0][0]

    return emocion_mas_comun


#Mejorar con GSI 
def getNmembers(dynamodb = db, N = 20):
    featureEmotions = []
    table_name = 't_miembros'
    response = dynamodb.scan(
        TableName=table_name,
        ProjectionExpression='code, nombre, area, puntaje, correo',  # Falta agregar emoción predominante (crear función)
        ExpressionAttributeNames={'#p': 'puntaje'},  # Nombre del atributo puntaje
        ExpressionAttributeValues={':val': {'N': '0'}},  # Filtro para puntaje mayor o igual a 0
        FilterExpression='#p >= :val',  # Filtro para puntaje mayor o igual a 0
    )

    # Ordena los elementos por puntaje de mayor a menor
    items = sorted(response['Items'], key=lambda x: int(x['puntaje']['N']), reverse=True)
    items = items[:N]
    #Separar en una función aparte
    for elem in items:
        # Extrae los valores necesarios de cada elemento
        codigo = elem.get('code', {}).get('S', '')
        nombre = elem.get('nombre', {}).get('S', '')
        area = elem.get('area', {}).get('S', '')
        puntaje = int(elem.get('puntaje', {}).get('N', '0'))
        correo = elem.get('correo', {}).get('S', '')

        # Crea un diccionario para el elemento actual
        elemento = {
            "codigo": codigo,
            "nombre": nombre,
            "area": area,
            "puntaje": puntaje,
            "correo": correo
        }

        # Agrega el elemento al diccionario resultante usando el código como clave
        featureEmotions.append(elemento)

    # Obtiene los N primeros elementos
    return featureEmotions

####################################################################################

def getMember(member_id, tenant_id = 'UTEC', dynamodb = db):
    table_name = 't_miembros'
    try:
        response = dynamodb.get_item(
            TableName=table_name,
            Key={'tenant_id': {'S': tenant_id}, 'code': {'S': member_id}},
        )
        print(response)
        item = response.get('Item')
        codigo = item.get('code', {}).get('S', '')
        nombre = item.get('nombre', {}).get('S', '')
        area = item.get('area', {}).get('S', '')
        puntaje = int(item.get('puntaje', {}).get('N', '0'))
        correo = item.get('correo', {}).get('S', '')

        member = {
            "codigo": codigo,
            "nombre": nombre,
            "area": area,
            "puntaje": puntaje,
            "correo": correo
        }
        return member
    except Exception as e:
        print(f"Error al obtener el registro: {e}")
        #return jsonify({"error": str(e), 'statusCode': 500})


def updateScoreByState(member_id, state, tenant_id = 'UTEC', dynamodb = db):
    table_name = 't_miembros'
    member = getMember(member_id)
    print(state, "-----------------------------")
    try:
        actual_score = int(member['puntaje'])
        print(actual_score, "-------------------------")
        new_score = calculateNewScore(actual_score, int(state))
        print(new_score, "--------------------------------")
        dynamodb.update_item(
            TableName=table_name,
            Key={
                'tenant_id': {'S': tenant_id}, 
                'code': {'S': member_id}
            },
            UpdateExpression='SET puntaje = :val1, estado = :val2',
            ExpressionAttributeValues={
                ':val1': {'N': str(new_score)},
                ':val2': {'N': str(state)}
            }
        )
        return new_score
    except Exception as e:
        print(f"Error al obtener el registro: {e}")

#Obtiene los registros para un determinado intervalo de tiempo, siempre tiene una fecha limite desde ahí hasta la actualidad
def getDataTiempo(dynamodb, tenant_id, fecha_limite):
    formatted_fecha_limite = fecha_limite.strftime('%Y-%m-%dT%H:%M:%S')
    table_name = 't_registro_emociones'

    response = dynamodb.scan(
        TableName=table_name,
        ProjectionExpression='emocion,code, fechaThora',
        ExpressionAttributeNames={'#fechaThora': 'fechaThora', '#tenant_id': 'tenant_id'},
        ExpressionAttributeValues={
            ':date': {'S': formatted_fecha_limite},
            ':tenant_id': {'S': tenant_id}
        },
        FilterExpression='#fechaThora >= :date and #tenant_id = :tenant_id',
    )
    return response['Items']

"""
#########################
#IGNORAR
#########################

def getXmainGrafico(fecha_limite = datetime(2023, 8, 20, 0,0,0)):
    end_date = datetime(2023, 8, 28, 0,0,0)
    fechaThora_list = []
    current_date = fecha_limite

    while current_date <= end_date:
        # Verificar si la hora actual está entre las 6 AM (6) y las 11 PM (23)
        if 6 <= current_date.hour <= 23:
            fechaThora_list.append(current_date.strftime('%Y-%m-%dT%H:%M:%S'))
        
        current_date += timedelta(hours=13)

    return fechaThora_list


def getValuesMainGrafico(dynamodb,fecha_limite, tenant_id = 'UTEC'):
    fechaThora_list = getXmainGrafico(fecha_limite)
    table_name = 't_registro_emociones'
    #diccionario

    valores = getDataTiempo(dynamodb, tenant_id, fecha_limite) #todos los valores sin filtrar por area o emocion 
    for i in range(len(valores)):
        pass


#solo cambia la emoción y el área
def mainGrafico(emocion = 'tristeza', area = 'Computer Science', items = getDataTiempo(db,'UTEC',fecha_limite = datetime(2023, 8, 20, 0, 0, 0)),dynamodb = db, tenant_id = 'UTEC'):
    emocion_ids = getEmocionesId(items)
    ids_emocion_actual = emocion_ids[emocion] #total ids que estan <emocion> en el intervalo de tiempo

    print(ids_emocion_actual)


#retorna un diccionario de listas, donde emocion es key y la lista de ids el valor 
def getEmocionesId(items):

    emocion_ids = defaultdict(list)

    for item in items:
        emocion = item['emocion']['S']
        id = item['code']['S']
        emocion_ids[emocion].append(id)

    return dict(emocion_ids)    


#mainGrafico()
"""