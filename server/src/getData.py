from database import dynamodb as db
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
            horarios[codigo] = horario
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



def actualizarPuntaje(dynamodb = db,tenant_id = 'UTEC'): #corregir debe sumar dado la ultima consulta, por ahora solo actualiza
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
    #fecha predeterminada últimos dos días

    pass
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