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



# == TAREA: INTEGRANTE B (Analista de Datos)

def agregar_pais(lista_paises):
    pass

def actualizar_pais(lista_paises):
    pass

def ordenar_paises(lista_paises):
    pass

def mostrar_estadisticas(lista_paises):
    pass


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