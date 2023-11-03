import boto3

# Configura tus credenciales de AWS
aws_access_key = 'ASIA6A6UW7LW7IIPWSOR'
aws_secret_key = 'OWTxQVJzevb4Ty1p5JJKN3mNvSw5iMwmtgZNxlsN'
aws_session_token = 'FwoGZXIvYXdzECkaDFEifZj5vIV506SBaCLNAdOL+O4BGrCdvN6U/cLCux7cpaFKyH1MoDyGPVR15wc8iA+3sU+qI7OnVCea3/FHNQvV5YjCirVesKSSvY+7Us8ALye9vmFTKdyfYmtdkJUQ4rLt5Hv2TvHzwjYiDA85lVMffm0hFs5nSq8Kuz2v8WYN9vydgctCB/cKNLIg2xmHgOLU2I0YqjjBszJR8t52xz3IwcQmb+BW63cI/fV7OVIKeQsEYGDygeQUZ1I3VOUUlXjgzhu6nFoP2RTo8rN4lAgW4KE0cIqDHE5OWn8o7vyVqgYyLVP6/Q9jNOgxDgkBEWqKjzRFV3ag10CRYi0emqdgp+ahRQKWtgL7e8qS//fesQ=='
region_name = 'us-east-1'

# Inicializa el cliente de DynamoDB
dynamodb = boto3.client('dynamodb',
                        aws_access_key_id=aws_access_key,
                        aws_secret_access_key=aws_secret_key,
                        aws_session_token = aws_session_token,
                        region_name=region_name)
