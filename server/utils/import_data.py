import pandas as pd
import requests

# Read the CSV using pandas
df = pd.read_csv('../data/members.csv')

# URL of your FastAPI API (make sure to replace localhost:8000 with the correct URL if it's different)
base_url = 'http://localhost:8000'
create_endpoint = '/member/create'

# Iterate over each row in the DataFrame and make a POST request
i = 0
for _, row in df.iterrows():
    if i == 50: break
    member_data = {
        "code": row['code'],
        "name": row['name'],
        "area": row['area'],
        "age": int(row['age']),
        "email": row['email'],
        "role": row['role']
    }
    print(member_data)
    response = requests.post(f'{base_url}{create_endpoint}', json=member_data)
    if response.status_code == 200:
        print(f'Member created successfully: {member_data}')
    else:
        print(f'Error creating member: {response.text}')
    i = i+1