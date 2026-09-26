# Catálogo de Piezas Coleccionables (v2)

## Objetivo del programa

Este programa permite gestionar un catálogo de piezas coleccionables por consola: 
registrar piezas nuevas, consultarlas, filtrarlas por estado o precio, calcular 
métricas del catálogo y eliminar piezas, todo con validación de los datos 
introducidos por el usuario.

Es la evolución de un proyecto anterior que usaba un único flujo de ejecución; 
en esta versión el código está organizado en funciones y separado en varios 
módulos (`catalog.py`, `validations.py`, `main.py`), aplicando manejo de 
errores con `try/except` y lanzamiento de excepciones con `raise`.

## Contexto del catálogo

El sistema está pensado para gestionar piezas coleccionables de cualquier tipo 
(figuras, cartas, monedas, etc.). Cada pieza tiene un identificador único, 
nombre, categoría, precio, estado (disponible, reservada o vendida) y una 
descripción que debe indicar si la pieza está usada o certificada.

## Funcionalidades implementadas

- Agregar una pieza nueva al catálogo, con validación de todos sus datos.
- Mostrar todas las piezas registradas.
- Mostrar únicamente las piezas disponibles.
- Calcular y mostrar el precio promedio del catálogo.
- Buscar una pieza por su identificador.
- Eliminar una pieza del catálogo por su identificador.
- Validaciones: campos obligatorios no vacíos, precio numérico y mayor que 
  cero (acepta coma o punto como separador decimal), estado dentro de los 
  permitidos (sin distinguir mayúsculas/minúsculas ni género), descripción 
  con la palabra "usada"/"usado" o "certificada"/"certificado", e id no 
  repetido dentro del catálogo.
- Manejo de errores: los datos inválidos no detienen el programa, se muestra 
  un mensaje claro y se puede volver a intentar desde el menú.

## Ejemplo de interacción

<img width="1582" height="607" alt="Captura de pantalla 2026-09-26 152551" src="https://github.com/user-attachments/assets/65e4c470-d0d3-4a90-8ca8-0afdef92e4cd" />

## Tecnologías utilizadas

- Python 3.14
- Sin librerías externas (solo funciones nativas del lenguaje)

## Cómo ejecutar el programa

1. Clona este repositorio:

https://github.com/Marisa-Ruiz/catalogo_coleccionables_v2.git

2. Entra en la carpeta del proyecto:

cd catalogo_coleccionables_v2

3. Ejecuta el archivo principal:

python main.py

4. Sigue las instrucciones del menú en pantalla.
