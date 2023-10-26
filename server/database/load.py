import boto3
import pandas as pd

aws_access_key = 'TU_ACCESS_KEY'
aws_secret_key = 'TU_SECRET_KEY'
region_name = '' 

dynamodb = boto3.client('dynamodb',
                        aws_access_key_id=aws_access_key,
                        aws_secret_access_key=aws_secret_key,
                        region_name=region_name)

df = pd.read_csv('./members.csv') 

for index, row in df.iterrows():
    item = {
        'code': row['code'], 
        'name': row['name'],
        'area': row['area'],
        'age': row['age'],
        'email': row['email'],
        'rol': row['rol']
    }

    dynamodb.put_item(TableName='members', Item=item)