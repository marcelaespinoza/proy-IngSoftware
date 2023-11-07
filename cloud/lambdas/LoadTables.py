from os import getenv
import boto3

# Config
dynamodb = boto3.resource('dynamodb',
         aws_access_key_id=getenv("aws_access_key_id"),
         aws_secret_access_key=getenv("aws_secret_access_key"),
         aws_session_token=getenv("aws_session_token"),
         region_name=getenv("aws_region_name"))

destination_dynamodb = boto3.resource('dynamodb') # my account

def load_table_member():
    source_table_name = 't_miembros'  
    destination_table_name = 'Member' 
    
    response = dynamodb.scan(
        TableName=source_table_name,
        ProjectionExpression='code, nombre, area, edad, correo, rol, estado, puntaje'
    )
    
    items = response['Items']

    destination_table = destination_dynamodb.Table(destination_table_name)
    
    for item in items:
        new_item = {
            'code': item['code'],
            'name': item['nombre'],
            'area': item['area'],
            'age': item['edad'],
            'email': item['correo'],
            'role': item['rol'],
            'state': item['estado'],
            'neg_score': item['puntaje']
        }
        
        destination_table.put_item(
            Item=new_item
        )
    
    return {
        'statusCode': 200,
        'body': 'Records copied successfully'
    }


def load_table_emotion_log():
    source_table_name = 't_registro_emociones'  
    destination_table_name = 'EmotionLog' 
    
    response = dynamodb.scan(
        TableName=source_table_name,
        ProjectionExpression='code, fechaThora, emocion'
    )
    
    items = response['Items']

    destination_table = destination_dynamodb.Table(destination_table_name)
    
    for item in items:
        new_item = {
            'member_code': item['code'],
            'timestamp': item['fechaThora'],
            'emotion': item['area']
        }
        
        destination_table.put_item(
            Item=new_item
        )
    
    return {
        'statusCode': 200,
        'body': 'Records copied successfully'
    }


def load_table_area():
    source_table_name = 't_areas'  
    destination_table_name = 'Area' 
    
    response = dynamodb.scan(
        TableName=source_table_name,
        ProjectionExpression='nombre'
    )
    
    items = response['Items']

    destination_table = destination_dynamodb.Table(destination_table_name)
    
    for item in items:
        new_item = {
            'nombre': item['nombre'],
            'description': {'S': 'description'}
        }
        
        destination_table.put_item(
            Item=new_item
        )
    
    return {
        'statusCode': 200,
        'body': 'Records copied successfully'
    }


def load_table_psychologist_schedule():
    source_table_name = 't_horarios_psicologos'  
    destination_table_name = 'PsychologistSchedule' 
    
    response = dynamodb.scan(
        TableName=source_table_name,
        ProjectionExpression='code, horario'
    )
    
    items = response['Items']

    destination_table = destination_dynamodb.Table(destination_table_name)
    
    for item in items:
        new_item = {
            'member_code': item['code'],
            'schedule': item['horario'],
        }
        
        destination_table.put_item(
            Item=new_item
        )
    
    return {
        'statusCode': 200,
        'body': 'Records copied successfully'
    }


def load_table_emotion():
    source_table_name = 't_emociones'  
    destination_table_name = 'Emotion' 
    
    response = dynamodb.scan(
        TableName=source_table_name,
        ProjectionExpression='nombre, valor'
    )
    
    items = response['Items']

    destination_table = destination_dynamodb.Table(destination_table_name)
    
    for item in items:
        new_item = {
            'name': item['nombre'],
            'score': item['valor']
        }
        
        destination_table.put_item(
            Item=new_item
        )
    
    return {
        'statusCode': 200,
        'body': 'Records copied successfully'
    }


def load_table_rol():
    source_table_name = 't_roles'  
    destination_table_name = 'Role' 
    
    response = dynamodb.scan(
        TableName=source_table_name,
        ProjectionExpression='nombre'
    )
    
    items = response['Items']

    destination_table = destination_dynamodb.Table(destination_table_name)
    
    for item in items:
        new_item = {
            'nombre': item['nombre'],
            'description': {'S': 'description'}
        }
        
        destination_table.put_item(
            Item=new_item
        )
    
    return {
        'statusCode': 200,
        'body': 'Records copied successfully'
    }


def lambda_handler(event, context):
    load_table_member()
    load_table_emotion_log()
    load_table_area()
    load_table_psychologist_schedule()
    load_table_emotion()
    load_table_rol()

