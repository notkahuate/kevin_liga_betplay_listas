equipos = []

def crear_equipo(nombre):
    if not any(equipo['nombre'] == nombre for equipo in equipos):
        equipos.append({
            'nombre': nombre,
            'pj': 0,
            'pg': 0,
            'pp': 0,
            'pe': 0,
            'gf': 0,
            'gc': 0,
            'puntos': 0
        })
        print(f"Equipo {nombre} registrado correctamente.")
    else:
        print(f"El equipo {nombre} ya está registrado.")
 
   


def mostrar_equipos():
    if equipos:
        print("\nEquipos registrados:")
        for equipo in equipos:
            print(f"- {equipo['nombre']}")
    else:
        print("No hay equipos registrados.")





