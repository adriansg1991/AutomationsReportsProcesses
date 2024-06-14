# Automatización de procesos/informes en Departamentos Contables/Financieros

[![Python Version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)
[![Pandas](https://img.shields.io/badge/pandas-1.2.0+-yellow)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-1.20.0-blue)](https://numpy.org/)
[![OpenpyXL](https://img.shields.io/badge/openpyxl-3.0.7-brightgreen)](https://openpyxl.readthedocs.io/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)](https://docs.python.org/3/library/tk.html)
[![Auto-py-to-exe](https://img.shields.io/badge/Auto--py--to--exe-2.10.0-green)](https://pypi.org/project/auto-py-to-exe/)


Es cierto que la automatización de tareas en departamentos contables/financieros puede ser muy beneficiosa. La implementación de tecnologías y herramientas automatizadas puede ahorrar tiempo, reducir errores humanos y permitir que los profesionales se centren en tareas más estratégicas y analíticas.

Gracias a haber aprendido a programar en Python, me permite mejorar este tipo de procesos manuales con el objetivo de automatizarlos.

Como he comentado en este post, voy a explicar 3 automatizaciones que he realizado.

## 📊 Proyecto 1: Informe de Productos Mensual

En la empresa donde trabajo actualmente, se requiere elaborar mensualmente un informe el primer día del mes que contenga un listado de todas las compañías del grupo, junto con las ventas correspondientes a una serie de productos que comercializamos.

### 1.1 ¿Cómo se hacía este informe manualmente?

Para poder hacer este informe de forma manual, hay que entrar en el CRM (web), descargar varios Excel y trabajar con los datos (operaciones, tablas dinámicas, etc.) para obtener la información. 

Por ejemplo, los productos, aparte de venderlos a clientes finales, también se venden a otros laboratorios del grupo. De esta manera, hay que restar estos importes para no duplicar ventas. Además de esta casuística, hay muchas más a tener en cuenta y que hacen que haya que transformar los datos y no pueda salir el informe directamente del CRM.

### 1.2 ¿Cómo automatizar este proceso?

Para que funcione el script y te genere las ventas mensuales por laboratorio, únicamente hay que indicar las fechas de inicio y final para extraer la información del CRM.

### 1.3 Librerías

Para poder automatizar este informe, he utilizado las siguientes librerías:

- **Selenium**: Para automatizar las acciones en la parte web. Esta librería simula el uso del ratón y el teclado en el navegador.
  - Abre Chrome e inserta la URL del CRM.
  - Se dirige a la pestaña que le indico.
  - Introduce la fecha inicial y final en el CRM para, posteriormente, generar un Excel, filtrando la información que necesitamos.
  - Finalmente, descarga el fichero.
  
- **Pandas/Numpy**: Utilizo estas librerías para trabajar con los datos descargados del CRM.
  - Selecciono las columnas que necesito y hago las operaciones necesarias que haría de forma manual en un Excel: sumar datos, restar, quitar filas, agrupar, etc. hasta llegar a los resultados que necesito.

A continuación, podéis ver un video donde se puede ver el proceso automatizado:

[![Automatización de Informe de Productos Mensual](https://img.youtube.com/vi/iPIPH-fp9_s/0.jpg)](https://youtu.be/iPIPH-fp9_s)

---

## 📊 Proyecto 2: Automatización de Carga Masiva de Facturas en SAP Business One

Otra automatización que he realizado es la automatización de la carga de facturas de forma masiva en SAP Business One. Para cargar facturas, SAP exige un archivo Excel con un formato específico. Tradicionalmente, los contables debían descargar la información de las facturas desde el CRM de la empresa, trabajar los datos en Excel, adaptarlos al formato requerido por SAP y luego cargarlos en el sistema.

Para simplificar y automatizar este proceso, he creado un programa con interfaz gráfica que actúa como un conversor. El objetivo del programa es cargar el archivo descargado del CRM, hacer clic en “convertir” y generar automáticamente el archivo Excel necesario para la carga en SAP, eliminando la necesidad de manipulación manual de los datos y reduciendo así el tiempo y los errores potenciales.

### 1. Funcionalidades

- **Carga del archivo CRM**: Permite cargar el archivo Excel exportado desde el CRM.
- **Conversión Automática**: Transforma los datos al formato requerido por SAP con un solo clic.
- **Interfaz de Usuario**: Proporciona una interfaz gráfica fácil de usar para los contables, eliminando la necesidad de trabajar manualmente con los datos.

### 2. Librerías Utilizadas

- **Pandas/Numpy**: Para leer el archivo Excel de facturas descargado del CRM y transformar los datos hasta obtener el formato requerido por SAP.
- **OpenpyXL**: Para dar formato al archivo final (formato de tabla, agrupación de celdas, etc.).
- **Tkinter**: Para crear una interfaz gráfica de usuario (GUI) con varios botones que facilitan el trabajo a los contables.
- **Auto-py-to-exe**: Para compilar el código y generar un ejecutable (.exe).

### 3. Ejemplo de Uso

1. **Carga del Archivo CRM**: Los usuarios cargan el archivo Excel descargado desde el CRM a través de la interfaz del programa.
2. **Conversión**: Hacen clic en el botón "Convertir" para transformar los datos automáticamente.
3. **Archivo Final**: El programa genera el archivo Excel en el formato correcto para ser cargado en SAP Business One.

### 4. Tecnologías y Herramientas

- **Lenguajes**: Python
- **Librerías**: pandas, numpy, openpyxl, tkinter
- **Herramientas de Desarrollo**: Auto-py-to-exe

### Excel extraído del CRM
![Automatización de Tareas](https://github.com/adriansg1991/Automatizaciones/blob/main/1.png)


### Excel para cargar en SAP
![Automatización Carga masiva fras. a SAP B1](https://github.com/adriansg1991/Automatizaciones/blob/main/2.png)

### 5. Programa — Conversor
![Automatización de Tareas](https://github.com/adriansg1991/Automatizaciones/blob/main/3.png)

A continuación, podéis ver un video donde se puede el programa que he creado que automatiza este proceso:
[![Imagen de vista previa del video](https://img.youtube.com/vi/UUBhiQdTuu0/0.jpg)](https://youtu.be/UUBhiQdTuu0)

### 5. Último paso

Con el Excel convertido al formato que pide SAP, sólo falta acceder a SAP y cargar el archivo. De esta manera, se contabilizarán todas las facturas de forma masiva.

---

## 📊 Proyecto 3: Cargar datos a una web a través de .csv/.xlsx
En la empresa actual donde trabajo, la introducción de datos en el CRM se hacia de forma manual. Este proceso es posible automatizarlo con Python.
Podemos realizar un script que se ocupe de leer un .CSV/excel y vaya rellenando los campos que le indiquemos del CRM (web).

Por ejemplo, en el CRM de la empresa, hay un campo donde indicamos el nº de interlocutor SAP.
En SAP, puedes sacar un listado con el CIF y nº de interlocutor, una vez han sido creados. De esta manera, podemos cargar este listado en el CRM de forma automática.
El script irá entrando en la ficha del interlocutor del CRM mediante el CIF y rellenará el nº de interlocutor.

En este ejemplo, queremos añadir los nº de interlocutor pero es posible adaptarlo para cualquier información que queramos añadir.

Código de ejemplo del script: [Repositorio Script carga datos a CRM](https://github.com/adriansg1991/Automatizaciones/blob/main/AddDataCRM.py)

