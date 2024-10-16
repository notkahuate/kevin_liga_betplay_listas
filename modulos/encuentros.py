from regis_equipo import equipos

encuentros = []

def programar_encuentro(equipo1, equipo2, dia, mes, ano):
    if any(equipo['nombre'] == equipo1 for equipo in equipos) and any(equipo['nombre'] == equipo2 for equipo in equipos):
        encuentros.append({
            'equipo1': equipo1,
            'equipo2': equipo2,
            'fecha': f"{dia}/{mes}/{ano}",
            'resultado': None
        })
        print(f"Encuentro entre {equipo1} y {equipo2} programado para {dia}/{mes}/{ano}.")
    else:
        print("Uno o ambos equipos no existen, verifique los nombres.")


def resultados_Encuentros(equipo1, equipo2, goles1, goles2):
    for encuentro in encuentros:
        if encuentro['equipo1'] == equipo1 and encuentro['equipo2'] == equipo2:
            encuentro['resultado'] = f"{goles1} - {goles2}"

            
            for equipo in equipos:
                if equipo['nombre'] == equipo1:
                    equipo['pj'] += 1
                    equipo['gf'] += goles1
                    equipo['gc'] += goles2
                    if goles1 > goles2:
                        equipo['pg'] += 1
                        equipo['puntos'] += 3
                    elif goles1 == goles2:
                        equipo['pe'] += 1
                        equipo['puntos'] += 1
                    else:
                        equipo['pp'] += 1
                elif equipo['nombre'] == equipo2:
                    equipo['pj'] += 1
                    equipo['gf'] += goles2
                    equipo['gc'] += goles1
                    if goles2 > goles1:
                        equipo['pg'] += 1
                        equipo['puntos'] += 3
                    elif goles1 == goles2:
                        equipo['pe'] += 1
                        equipo['puntos'] += 1
                    else:
                        equipo['pp'] += 1

            print(f"Resultado registrado: {equipo1} {goles1} - {goles2} {equipo2}")
            return

    print("El encuentro no está programado.")

def mostrar_tabla():
    print("\nTabla de posiciones:")
    print("Equipo | PJ | PG | PP | PE | GF | GC | Pts")
    for equipo in equipos:
        print(f"{equipo['nombre']}: PJ: {equipo['pj']}, PG: {equipo['pg']}, PP: {equipo['pp']}, PE: {equipo['pe']}, GF: {equipo['gf']}, GC: {equipo['gc']}, Puntos: {equipo['puntos']}")
   