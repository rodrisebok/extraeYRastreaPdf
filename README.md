## Descripción

Este proyecto consiste en una herramienta en Python para facilitar la **conciliación bancaria** automatizando la extracción de datos de **extractos en formato PDF**.

El script procesa un archivo PDF y extrae información de los movimientos bancarios, como pagos, transferencias, comisiones y otros cargos, para calcular automáticamente montos totales y generar reportes de manera eficiente.

## Tecnologías
- **Python**
- **PyPDF2** (para extraer texto de archivos PDF)
- **Re**

## Cómo Funciona
1. El script lee el archivo PDF con el extracto bancario.
2. Extrae los datos clave de las transacciones como:
   - Pagos
   - Transferencias
   - Comisiones
   - Impuestos
3. Realiza cálculos de los montos por cada concepto.
5. El programa devuelve los resultados solicitados en la terminal.

## Instrucciones de Uso
### Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tuusuario/conciliacion-bancaria-python.git
    ```

2. Instala las dependencias necesarias:
    ```bash
    pip install PyPDF2
    ```

3. Coloca el archivo PDF con el extracto bancario en la misma carpeta que el script o indica su ruta correcta en el código. Es importante colocarle el nombre "extracto.pdf" al archivo que vamos a analizar.

4. Ejecuta el script:

5. Introduce el concepto que deseas calcular para obtener el cálculo.
