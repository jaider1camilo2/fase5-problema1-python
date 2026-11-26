# ------------------------------------------------------------
# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema 1: Clasificación del compromiso de sesiones
# Estudiante: Jaider Camilo Padilla Santana
# Grupo: 213022_372
# ------------------------------------------------------------


def clasificar_compromiso(duracion, clics):
    """
    Determina el nivel de compromiso de una sesión.

    Parámetros:
        duracion (int): duración de la sesión en segundos.
        clics (int): cantidad de clics realizados.

    Retorna:
        str: "Alto", "Bajo" o "Medio".
    """

    if duracion > 180 and clics > 8:
        nivel = "Alto"
    elif duracion < 60 or clics < 3:
        nivel = "Bajo"
    else:
        nivel = "Medio"

    return nivel


# Matriz de sesiones:
# [ID del cliente, duración en segundos, número de clics]
sesiones = [
    ["CLI001", 240, 12],
    ["CLI002", 45, 6],
    ["CLI003", 150, 7],
    ["CLI004", 200, 2],
    ["CLI005", 300, 15],
    ["CLI006", 90, 4]
]


# Inicialización del contador
i = 0


# Configuración del ancho de las columnas
ancho_id = 20
ancho_compromiso = 15
ancho_total = ancho_id + ancho_compromiso


# Presentación del encabezado del informe
print("=" * ancho_total)
print("INFORME DE COMPROMISO DE SESIONES".center(ancho_total))
print("=" * ancho_total)
print(f"{'ID DEL CLIENTE':<{ancho_id}}"
      f"{'COMPROMISO':<{ancho_compromiso}}")
print("-" * ancho_total)


# Recorrido de la matriz y clasificación de cada sesión
while i < len(sesiones):

    # Extraer los datos de la sesión actual
    id_cliente, duracion, clics = sesiones[i]

    # Clasificar el compromiso de la sesión
    clasificacion = clasificar_compromiso(duracion, clics)

    # Mostrar el resultado de la sesión
    print(
        f"{id_cliente:<{ancho_id}}"
        f"{clasificacion:<{ancho_compromiso}}"
    )

    # Pasar a la siguiente sesión
    i += 1


# Resumen y finalización del informe
print("-" * ancho_total)
print(f"Total de sesiones procesadas: {i}")
print("=" * ancho_total)