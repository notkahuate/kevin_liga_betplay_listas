from regis_equipo import equipos

cuerpo_tecnicos =[]

def crear_tecnico(nombre,equipo_tc):
    if any(equipo['nombre'] == equipo_tc for equipo in equipos):
        cuerpo_tecnicos.append({
            'nombre': nombre,
            'equipo': equipo_tc
        })
        print(f"Cuerpo técnico {nombre} registrado en el equipo {equipo_tc}.")
    else:
        print(f"El equipo {equipo_tc} no está registrado.")



def motrar_tc():
   if cuerpo_tecnicos:
        print("\nCuerpos técnicos registrados:")
        for cuerpo in cuerpo_tecnicos:
            print(f"- Nombre: {cuerpo['nombre']}, Equipo: {cuerpo['equipo']}")
   else:
        print("No hay cuerpos técnicos registrados.")


