import csv
numero= int(input("Ingresa la cantidad de miembros que quieres que se guarde: "))
#diccionario de las emociones con sus puntajes
emociones_puntajes = {
    'tristeza': 10,
    'estres': 4,
    'ansiedad': 5,
    'frustracion': 5,
    'enojo': 8,
    'aburrimiento': 2,
    'preocupacion': 3,
    'motivacion': -5,
    'felicidad': -10,
    'satisfaccion': -4,
    'alivio': -2
}

with open('../server/registroEmociones.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)
        datos_puntajes = {}
        for fila in lector_csv:
            codigo = fila[0]
            emocion = fila[1]
            # Calcula el puntaje usando el diccionario de emociones_puntajes
            puntaje = emociones_puntajes.get(emocion, 0)
            print()
            print(puntaje)
            print()
            # Si el código ya está en el diccionario, agrega el puntaje
            if codigo in datos_puntajes:
                datos_puntajes[codigo] += puntaje
            # Si el código no está en el diccionario, crea una nueva entrada
            else:
                datos_puntajes[codigo] = puntaje

# Ordena los códigos según los puntajes de mayor a menor
codigos_ordenados = sorted(datos_puntajes.items(), key=lambda x: x[1], reverse=True)

"""
# Escribir los códigos y puntajes ordenados
with open('../server/codigos_puntajes_ordenados.csv', 'w', newline='') as archivo_csv_puntajes:
    escritor_csv = csv.writer(archivo_csv_puntajes)
    # Escribe los datos en el nuevo archivo CSV con los n primeros miembros
    n=0
    for codigo, puntaje in codigos_ordenados:
        if(n<numero):
            escritor_csv.writerow([codigo, puntaje])
        n+=1
"""