import boto3

# Configura tus credenciales de AWS
aws_access_key = 'ASIA6A6UW7LW4TLMESQN'
aws_secret_key = '4q7974poi1j0Mftfz26DflqQC6qtcg/15FIS0rLG'
aws_session_token = 'FwoGZXIvYXdzECQaDMU8mOf4H8lCTb96TSLNAZ38Eg3c5TLPid2dHW//boKOUJfP1F1Wx+tXe3dcY/YhwdpY4gbu+D/KU0ZbjYPIEPj2H0nkfpWqRisI//3GSMn6JghgzTdVQSfo5nPODLfbddoVeJs59R7IRC999DLG65Kp/ykeTzxdhSTJqqv3MuUBgFX2wnnq9s2YOLdV67QIaeAYRbHzuunB68p1q1kNoY0CGlA1BvLAss6VCkLcSXxd8KNINMkDkZRNQKJkG+PkJuE3TQmSqMlV+bfpHCddZCac6IubfkoUB9FWo+AoqYWVqgYyLQoFYtmxfzy7m8EHmgndmAZlYedUboWvyY0Nn9r6KtzDivM5SRdPI/gFH0PWHA=='
region_name = 'us-east-1'

# Inicializa el cliente de DynamoDB
dynamodb = boto3.client('dynamodb',
                        aws_access_key_id=aws_access_key,
                        aws_secret_access_key=aws_secret_key,
                        aws_session_token = aws_session_token,
                        region_name=region_name)