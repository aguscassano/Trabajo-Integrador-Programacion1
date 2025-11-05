import csv
import os

# == TAREA: INTEGRANTE A (Arquitecto de Datos)

def cargar_datos_csv(nombre_archivo):

    lista_paises = []

    if not os.path.exists(nombre_archivo):
        print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
        return [] 

    with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
        lector_csv = csv.DictReader(archivo)

        for fila in lector_csv:
            
            poblacion_str = fila['poblacion']
            superficie_str = fila['superficie']

            if poblacion_str.isdigit() and superficie_str.isdigit():
                
                fila['poblacion'] = int(poblacion_str)
                fila['superficie'] = int(superficie_str)
                
                lista_paises.append(fila)
            else:
                print(f"Error de formato en fila: {fila}. Se omitirá este país.")
                continue 
    
    print(f"Se cargaron {len(lista_paises)} países.")
    return lista_paises

def buscar_pais(lista_paises):
    print("--- 3. Buscar país por nombre ---")

    termino_busqueda = input("Ingresa el nombre del país a buscar: ").strip().lower()

    if not termino_busqueda:
        print("Error: No ingresaste un término de búsqueda.")
        return
    
    resultados = []

    for pais in lista_paises:
        if termino_busqueda in pais["nombre"].lower():
            resultados.append(pais)

    print("--- Resultados de la busqueda ---")

    if not resultados:
        print(f"No se encontraron países que coincidan con {termino_busqueda}.")
    else:
        print(f"Se encontraron {len(resultados)} países: ")

        for pais_encontrado in resultados:
            print(f"Nombre: {pais_encontrado['nombre']}")
            print(f"Continente: {pais_encontrado['continente']}")
            print(f"Población: {pais_encontrado['poblacion']:,}")
            print(f"Superficie: {pais_encontrado['superficie']:,} km2")

    print("-"*30)

# --- FILTRAR PAISES ---

def filtrar_por_continente(lista_paises):
    print("--- Filtro por continentes ---")
    continente_buscando = input("Ingrese el nombre del continente: ").strip().lower()

    if not continente_buscando:
        print("Error: No ingresaste un continente.")
        return
    
    resultados = []

    for pais in lista_paises:
        if pais["continente"].lower() == continente_buscando:
            resultados.append(pais)

    if not resultados:
        print(f"No se encontraron paises en el continente '{continente_buscando}'")
    else:
        print(f"Se encontraron {len(resultados)} países en {continente_buscando}")
        for pais in resultados:
            print(f"-{pais['nombre']} (Pob: {pais['poblacion']:,})")

def filtrar_por_rango_poblacion(lista_paises):
    print("--- Filtro por rango de población ---")

    pob_min = obtener_entero_valido("Ingrese la población MÍNIMA: ")
    pob_max = obtener_entero_valido("Ingrese la población MÁXIMA: ")

    if pob_min > pob_max:
        print("Error: La población mínima no puede ser mayor a la población máxima.")
        return
    
    resultados = []

    for pais in lista_paises:
        if pob_min <= pais["poblacion"] <= pob_max:
            resultados.append(pais)

    if not resultados:
        print(f"No se encontraron países con población entre {pob_min:,} y {pob_max:,}.")
    else:
        print(f"Se encontraron {len(resultados)} países en ese rango de población:")
        for pais in resultados:
            print(f"-{pais['nombre']} (Pob: {pais['poblacion']:,})")

def filtrar_por_rango_superficie(lista_paises):
    print("--- Filtro por rango de superficie ---")

    sup_min = obtener_entero_valido("Ingrese la superficie MÍNIMA (km2): ")
    sup_max = obtener_entero_valido("Ingrese la superficie MÁXIMA (km2): ")

    if sup_min > sup_max:
        print("Error: La superficie mínima no puede ser mayor a la superficie máxima.")
        return
    
    resultados = []

    for pais in lista_paises:
        if sup_min <= pais["superficie"] <= sup_max:
            resultados.append(pais)

    if not resultados:
        print(f"No se encontraron países con superficie entre {sup_min:,} y {sup_max:,}")
    else:
        print(f"Se encontraron {len(resultados)} países en ese rango de superficie: ")
        for pais in resultados:
            print(f"-{pais['nombre']} (Superficie: {pais['superficie']:,} km2)")

def filtrar_paises(lista_paises):
    print("--- Filtrar países ---")
    print("1. Filtrar por continente")
    print("2. Filtrar por rango de población")
    print("3. Filtrar por rango de superficie")
    print("4. Volver al menú principal")
    print("-"*30)

    opcion = input("Elige una opción de filtro (1-4): ").strip()

    if opcion == "1":
        filtrar_por_continente(lista_paises)
    elif opcion == "2":
        filtrar_por_rango_poblacion(lista_paises)
    elif opcion == "3":
        filtrar_por_rango_superficie(lista_paises)
    elif opcion == "4":
        return
    else:
        print("Error: Opción no válida")

    input("Presione Enter para continuar...")

# HELPERS

def obtener_entero_valido(mensaje_input):
    while True:

        valor_str = input(mensaje_input).strip()

        if valor_str.isdigit():
            valor_int = int(valor_str)
            if valor_int > 0:
                return valor_int 
            else:
                print("Error: El número debe ser positivo (mayor a 0).")
        else:
            print("Error: Debes ingresar un número entero y positivo.")


def obtener_string_no_vacio(prompt):
    while True:
        valor = input(prompt).strip() # .strip() elimina espacios en blanco
        if valor:
            return valor
        else:
            print("Error: Este campo no puede estar vacío. Intente de nuevo.")


# --- HELPERS PARA ORDENAMIENTO ---
def obtener_key_nombre(pais):
    return pais["nombre"].lower()

def obtener_key_poblacion(pais):
    return pais["poblacion"]

def obtener_key_superficie(pais):
    return pais["superficie"]




# == TAREA: INTEGRANTE B (Analista de Datos)

def agregar_pais(lista_paises):
    print("\n--- 1. Agregar Nuevo País ---")
    
    nombre = obtener_string_no_vacio("Ingrese el nombre del país: ")
    
    # Validación extra: Verificar si el país ya existe
    encontrado = False
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"Error: El país '{nombre}' ya existe en la lista.")
            encontrado = True
            break
            
    if not encontrado:
        # Si no se encontró, pedimos el resto de los datos
        poblacion = obtener_entero_valido(f"Ingrese la población de {nombre}: ")
        superficie = obtener_entero_valido(f"Ingrese la superficie (km²) de {nombre}: ")
        continente = obtener_string_no_vacio(f"Ingrese el continente de {nombre}: ")
        
        # Creamos el diccionario del nuevo país
        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        
        lista_paises.append(nuevo_pais)
        
        print(f"¡Éxito! País '{nombre}' agregado correctamente.")

def actualizar_pais(lista_paises):
    print("\n--- 2. Actualizar Datos de País ---")
    
    if not lista_paises:
        print("Error: No hay países cargados en la lista.")
        return

    nombre_buscar = obtener_string_no_vacio("Ingrese el nombre del país que desea actualizar: ")

    pais_encontrado = None
    
    # 1. Buscamos el país en la lista
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            pais_encontrado = pais
            break 

    # 2. Verificamos si se encontró
    if pais_encontrado:
        print(f"País encontrado: {pais_encontrado['nombre']}")
        print(f"Datos actuales -> Población: {pais_encontrado['poblacion']: ,} | Superficie: {pais_encontrado['superficie']: ,} km²")
        
        # 3. Pedimos los nuevos datos
        nueva_poblacion = obtener_entero_valido(f"Ingrese la NUEVA población (actual: {pais_encontrado['poblacion']: ,}): ")
        nueva_superficie = obtener_entero_valido(f"Ingrese la NUEVA superficie km² (actual: {pais_encontrado['superficie']: ,}): ")
        
        # 4. Actualizamos el diccionario
        pais_encontrado["poblacion"] = nueva_poblacion
        pais_encontrado["superficie"] = nueva_superficie
        
        print(f"¡Éxito! Datos de '{pais_encontrado['nombre']}' actualizados.")
    
    else:
        # 5. Si no se encontró
        print(f"Error: País '{nombre_buscar}' no encontrado en la lista.")

def ordenar_paises(lista_paises):
    print("\n--- 5. Ordenar Países ---")
    
    if not lista_paises:
        print("Error: No hay países cargados para ordenar.")
        return

    print("Seleccione el criterio de ordenamiento:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    
    criterio = ""
    while criterio not in ["1", "2", "3"]:
        criterio = input("Ingrese una opción (1-3): ").strip()
        if criterio not in ["1", "2", "3"]:
            print("Opción inválida. Intente de nuevo.")

    orden = ""
    while orden not in ["A", "D"]:
        orden = input("Seleccione el orden (A para Ascendente, D para Descendente): ").strip().upper()
        if orden not in ["A", "D"]:
            print("Opción inválida. Intente de nuevo.")

    es_descendente = (orden == "D")
    
    if criterio == "1":
        lista_paises.sort(key=obtener_key_nombre, reverse=es_descendente)
        criterio_texto = "Nombre"
        
    elif criterio == "2":
        lista_paises.sort(key=obtener_key_poblacion, reverse=es_descendente)
        criterio_texto = "Población"
        
    elif criterio == "3":
        lista_paises.sort(key=obtener_key_superficie, reverse=es_descendente)
        criterio_texto = "Superficie"

    orden_texto = "Descendente" if es_descendente else "Ascendente"
    
    print(f"\n¡Éxito! Lista de países ordenada por {criterio_texto} en orden {orden_texto}.")
    
    # Mostramos los resultados del ordenamiento
    print("--- Resultados del Ordenamiento ---")
    for pais in lista_paises:
        if criterio == "1":
            print(f"- {pais['nombre']}")
        elif criterio == "2":
            print(f"- {pais['nombre']}: {pais['poblacion']: ,} habitantes")
        elif criterio == "3":
            print(f"- {pais['nombre']}: {pais['superficie']: ,} km²")

def mostrar_estadisticas(lista_paises):
    print("\n--- 6. Mostrar Estadísticas ---")
    
    if not lista_paises:
        print("Error: No hay países cargados para calcular estadísticas.")
        return

    # 1. Inicializamos las variables para los cálculos
    total_paises = len(lista_paises)
    total_poblacion = 0
    total_superficie = 0
    
    pais_max_poblacion = lista_paises[0]
    pais_min_poblacion = lista_paises[0]
    
    conteo_continentes = {}

    # 2. Recorremos la lista
    for pais in lista_paises:
        poblacion = pais["poblacion"]
        superficie = pais["superficie"]
        continente = pais["continente"]

        total_poblacion += poblacion
        total_superficie += superficie
        
        if poblacion > pais_max_poblacion["poblacion"]:
            pais_max_poblacion = pais
        
        if poblacion < pais_min_poblacion["poblacion"]:
            pais_min_poblacion = pais
            
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1

    # 3. Calculamos los promedios
    promedio_poblacion = total_poblacion / total_paises
    promedio_superficie = total_superficie / total_paises

    # 4. Mostramos todos los resultados
    print(f"Total de países en la lista: {total_paises}")
    print("\n--- Población ---")
    print(f"País con MAYOR población: {pais_max_poblacion['nombre']} ({pais_max_poblacion['poblacion']: ,} hab.)")
    print(f"País con MENOR población: {pais_min_poblacion['nombre']} ({pais_min_poblacion['poblacion']: ,} hab.)")
    print(f"Promedio de población: {promedio_poblacion:,.2f} habitantes")

    print("\n--- Superficie ---")
    print(f"Promedio de superficie: {promedio_superficie:,.2f} km²")


    print("\n--- Conteo por Continente ---")
    # Ordenamos el diccionario de continentes alfabéticamente
    for continente, cantidad in sorted(conteo_continentes.items()):
        print(f"- {continente}: {cantidad} país(es)")


# == TAREA: INTEGRANTE A (Arquitecto de Datos)
def mostrar_menu():
    print("--- DATOS DE PAÍSES ---")
    print("1. Agregar país")
    print("2. Actualizar datos de país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países (por continente, población, superficie)")
    print("5. Ordenar países (por continente, población, superficie)")
    print("6. Mostrar estadísticas")
    print("7. Salir")

    return input ("Seleccione una opción (1-7): ").strip()

def main ():

    archivo_csv = "archivo-paises.csv"

    mis_paises = cargar_datos_csv(archivo_csv)

    if not mis_paises:
        print(f"Error. No se pudieron cargar los datos desde {archivo_csv}.")
        return
    
    while True:
        opcion = mostrar_menu()

        match opcion:
            case "1":
                agregar_pais(mis_paises)
            case "2":
                actualizar_pais(mis_paises)
            case "3":
                buscar_pais(mis_paises)
            case "4":
                filtrar_paises(mis_paises)
            case "5":
                ordenar_paises(mis_paises)
            case "6":
                mostrar_estadisticas(mis_paises)
            case "7":
                print("Gracias por usar el programa!")
                break
            case _:
                print("Opción inválida. Vuelva a intentarlo.")


if __name__ == "__main__":
    main()