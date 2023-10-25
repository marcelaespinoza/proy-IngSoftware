from faker import Faker
from random import choice

faker = Faker("pe_PE")

# las areas se visualizan de la web asignando la cantidad y las carreras
# se asignan 12 para este caso

carrers = ["Administración", "Bioingeniería", "Ing. Ambiental", "Ing. Química", "Ing. Civil"] + \
    ["Computer Science", "Ing. Industrial", "Ing. Mecánica", "Ing. Energía" , "Ing. Mecatrónica", "Ing. Electrónica", "Data Science"]

# generar 400 miembros
members = []

for i in range(400):
    # modelo de dato en formato json para database dynamodb con tenant_id

    member = {
        "tenant_id": faker.uuid4(),
        "body": {
            "name": faker.name(),
            "carrer": choice(carrers),
            "age":  faker.random_int(min=18, max=30),
        }
    }