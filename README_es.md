# Descripción del programa

El programa toma un Excel que contiene precios de productos. Los transforma a un formato especial para poder ser insertados en el programa de facturación. 
La primera columna llamada 'Codigo' contiene el código del producto, y las siguientes columnas son las diferentes listas de precios que se deben modificar, cada una con el precio que deben tener para ese producto. Cada lista de precios se guarda en un archivo por separado.

## Ejemplo del archivo Excel

    Codigo      1      2       4       5      7      8     9     15
0     0039    169    172   176.0   158.0    180    150   172    142
1     0040    344    350   359.0   323.0    367    307   350    289
2     0041    654    666   683.0   615.0    700    584   666    551

# Script de División de Datos

Este script en Python toma el archivo Excel ubicado en la carpeta 'Input', donde se espera que tenga la columna 'Codigo' seguido de n columnas de las listas que se van a modificar, y crea un archivo de texto (.prn) para cada columna adicional (excepto 'Codigo'). Los archivos de texto generados se almacenan en la carpeta 'Output'.

## Funcionamiento

1. **Entrada de Datos:**
    - Se utiliza la función `get_files(folder)` para obtener la ruta del archivo Excel en la carpeta 'Input'.
    - Se lee el archivo Excel usando `pd.read_excel()`. La columna 'Codigo' se trata como cadena ('str').

2. **Creación de Archivos .prn:**
    - Se itera sobre las columnas del DataFrame, excluyendo la columna 'Codigo'.
    - Para cada columna, se crea un archivo de texto (.prn) que contiene información formateada de cada fila del DataFrame.

3. **Formato del Archivo .prn:**
    - Cada archivo .prn tiene el nombre 'L' seguido del nombre de la columna correspondiente.
    - Cada línea del archivo contiene:
        - 10 espacios para el nombre de la columna.
        - 12 espacios para el valor en la columna 'Codigo'.
        - 44 espacios para el valor en la columna actual.
        - Salto de línea al final de cada fila.

4. **Almacenamiento:**
    - Los archivos .prn se guardan en la carpeta 'Output' en el directorio actual.

## Ejecución

El script se ejecuta al correr el archivo y realiza la división de datos según el esquema descrito.

## Requisitos

- Python 3.x
- Pandas