import pandas as pd

# Read the CSV using pandas
df = pd.read_csv('../data/members.csv')

# Agregar una nueva columna 'NuevaColumna' con ceros
df['emotion_score'] = 0

#print(df.head(1000))

# Guardar el DataFrame actualizado
df.to_csv("../data/members2.csv", index=False)
