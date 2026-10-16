destinos = [
    {"nombre": "Granada", "tipo": "ciudad", "coste": 180, "dias": 2},
    {"nombre": "Cádiz", "tipo": "playa", "coste": 150, "dias": 3},
    {"nombre": "Pirineos", "tipo": "montaña", "coste": 220, "dias": 3},
    {"nombre": "Asturias", "tipo": "naturaleza", "coste": 200, "dias": 4}
]
def destinos_disponibles(destinos):
    print("Destinos disponibles:")
    for destino in destinos:
        print(f"- {destino['nombre']} ({destino['tipo']}) - Coste: {destino['coste']}€ - Días: {destino['dias']}") 

def agregar_destino(destinos): 
    nombre = input("Ingrese el nombre del destino: ")
    tipo = input("Ingrese el tipo de destino (ciudad/playa/montaña/naturaleza): ")
    coste = int(input("Ingrese el coste del destino: "))
    dias = int(input("Ingrese la cantidad de días para el destino: "))
    destinos.append({"nombre": nombre, "tipo": tipo, "coste": coste, "dias": dias})
    print(f"Destino {nombre} agregado exitosamente.") 

def tipo_destino (destino):  
  if not destino:
    print("No se ha ingresado un tipo de destino.")
    return
  buscar_destino = input("Ingrese el tipo de destino a buscar (ciudad/playa/montaña/naturaleza):")

    

# destinos_disponibles(destinos)

# agregar_destino(destinos) 
