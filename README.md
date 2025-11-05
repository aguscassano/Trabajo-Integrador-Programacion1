TPI Programación 1 - Gestión de Datos de Países
Tecnicatura Universitaria en Programación - UTN

Descripción del Programa
Esta es una aplicación de consola desarrollada en Python como parte del Trabajo Práctico Integrador (TPI) de la materia Programación 1.

El sistema permite gestionar un conjunto de datos de países, cargados desde un archivo CSV. Ofrece un menú interactivo en consola para realizar las siguientes operaciones:

Agregar nuevos países (con validación de entradas).

Actualizar la población y superficie de un país existente.

Buscar países por nombre (coincidencia parcial o exacta).


Filtrar países por continente, rango de población o rango de superficie .


Ordenar la lista de países por nombre, población o superficie (ascendente o descendente) .


Mostrar estadísticas clave (promedios, max/min, conteo por continente) .

Instrucciones de Uso
Requisitos:

Tener Python 3.x instalado en su sistema.

El archivo archivo-paises.csv  (incluido en este repositorio) debe estar ubicado en la misma carpeta que el script main.py.

Clonar el Repositorio:

Bash

git clone https://github.com/aguscassano/Trabajo-Integrador-Programacion1.git
cd Trabajo-Integrador-Programacion1
Ejecutar el Programa: En una terminal
Bash

python main.py
Navegación: Una vez ejecutado, se desplegará un menú en la consola. Ingrese el número de la opción deseada (1-7) y presione Enter para continuar.

⌨️ Ejemplos de Entradas y Salidas 

Menú Principal:

--- DATOS DE PAÍSES ---
1. Agregar país
2. Actualizar datos de país
3. Buscar país por nombre
4. Filtrar países (por continente, población, superficie)
5. Ordenar países (por continente, población, superficie)
6. Mostrar estadísticas
7. Salir
Seleccione una opción (1-7): 
Ejemplo: Opción 3 (Buscar país)

Seleccione una opción (1-7): 3
--- 3. Buscar país por nombre ---
Ingresa el nombre del país a buscar: arg

--- Resultados de la busqueda ---
Se encontraron 1 países: 
Nombre: Argentina
Continente: América
Población: 45,376,763
Superficie: 2,780,400 km2
------------------------------
Ejemplo: Opción 6 (Mostrar estadísticas)

Seleccione una opción (1-7): 6

--- 6. Mostrar Estadísticas ---
Total de países en la lista: 4
--- Población ---
País con MAYOR población: Nigeria (206,139,589 hab.)
País con MENOR población: Argentina (45,376,763 hab.)
Promedio de población: 115,116,420.75 habitantes
--- Superficie ---
Promedio de superficie: 1,059,241.25 km²
--- Conteo por Continente ---
- América: 1 país(es)
- Asia: 1 país(es)
- África: 1 país(es)
- Europa: 1 país(es)
👥 Integrantes y Participación 

Este proyecto fue desarrollado en equipo por 2 personas:

Agustin Cassano - "El Arquitecto de Datos")

Carga inicial de datos desde CSV (cargar_datos_csv).

Función de búsqueda de país (buscar_pais).

Funciones de filtrado (continente, población, superficie) (filtrar_paises).

Implementación del menú principal y flujo del programa (main, mostrar_menu).

Neyen Maleh - "El Analista de Datos"

Función de agregar un nuevo país con validaciones (agregar_pais).

Función de actualización de datos de país (actualizar_pais).

Funciones de ordenamiento por múltiples criterios (ordenar_paises).

Función de cálculo y muestra de estadísticas (mostrar_estadisticas).
