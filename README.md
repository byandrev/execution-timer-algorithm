# Script para la ejecucion de los tests

## Importante

Antes de ejecutar el script borren los archivos que estan dentro de la carpeta output.

## Requisitos

* Instalar: Java, PHP, Python, NodeJS y C++.
* Ejecutar en la consola `javac -version`. (Debe mostrar un número con la versión)
* Ejecutar en la consola `c++ --version`. (Debe mostrar un número con la versión)

## Pasos:

- 1. Ejecuta `python script.py` en la consola dentro de esta carpeta.
- 2. Los resultados quedaran en la carpeta output.

## Funcionamiento

El script `generate_tests.py` genera los inputs para cada test en un archivo txt dentro de la carpeta inputs, donde primero viene el tamaño de la matriz, seguido por un guion bajo y el número del test, por ejemplo `2_1.txt`.

El script `script.py` genera los tiempos de cada test. Esto lo hace con ayuda de las librerias `subprocess` y `datetime`. Subprocess tiene un método llamado check_output el cuál nos permite ejecutar comandos de terminar en python. Medimos el tiempo actual antes de ejecutar el comando y los restamos después de finalizar el comando, con esto se obtiene el tiempo de ejecución de cada test es segundos (s).
