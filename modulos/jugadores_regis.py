from regis_equipo import equipos

jugadores = []

def crear_jugador(nombre,dorsal,posicion,equipo_jgd):

    if any(equipo['nombre'] == equipo_jgd for equipo in equipos):
        jugadores.append({
            'nombre': nombre,
            'dorsal': dorsal,
            'posicion': posicion,
            'equipo': equipo_jgd,
            'tarjeta Amarillas' :0,
            'tarjeta Rojas' : 0,
            'Goles': 0
        })
        print(f"Jugador {nombre} registrado en el equipo {equipo_jgd}.")
    else:
        print(f"El equipo {equipo_jgd} no está registrado.")



   
def mostrar_jugadores():
   if jugadores:
        print("\nJugadores registrados:")
        for jugador in jugadores:
            print(f"- Nombre: {jugador['nombre']}, Dorsal: {jugador['dorsal']}, Posición: {jugador['posicion']}, Equipo: {jugador['equipo']}")

   else:
        print("No hay jugadores registrados.")



 