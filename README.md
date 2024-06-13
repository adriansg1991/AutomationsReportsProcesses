# Automatización de Tareas en Departamentos Contables/Financieros

Es cierto que la automatización de tareas en departamentos contables/financieros puede ser muy beneficiosa. La implementación de tecnologías y herramientas automatizadas puede ahorrar tiempo, reducir errores humanos y permitir que los profesionales se centren en tareas más estratégicas y analíticas.

Gracias a haber aprendido a programar en Python, me permite mejorar este tipo de procesos manuales con el objetivo de automatizarlos.

Como he comentado en este post, voy a explicar 3 automatizaciones que he realizado.

## Proyecto 1: Informe de Productos Mensual

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

## Proyecto 2: Automatización de Carga Masiva de Facturas en SAP Business One

Otra automatización que he realizado es la automatización de la carga de facturas de forma masiva en SAP Business One. Para cargar facturas, SAP exige un archivo Excel con un formato específico. Tradicionalmente, los contables debían descargar la información de las facturas desde el CRM de la empresa, trabajar los datos en Excel, adaptarlos al formato requerido por SAP y luego cargarlos en el sistema.

Para simplificar y automatizar este proceso, he creado un programa con interfaz gráfica que actúa como un conversor. El objetivo del programa es cargar el archivo descargado del CRM, hacer clic en “convertir” y generar automáticamente el archivo Excel necesario para la carga en SAP, eliminando la necesidad de manipulación manual de los datos y reduciendo así el tiempo y los errores potenciales.

### Funcionalidades

- **Carga del archivo CRM**: Permite cargar el archivo Excel exportado desde el CRM.
- **Conversión Automática**: Transforma los datos al formato requerido por SAP con un solo clic.
- **Interfaz de Usuario**: Proporciona una interfaz gráfica fácil de usar para los contables, eliminando la necesidad de trabajar manualmente con los datos.

### Librerías Utilizadas

- **Pandas/Numpy**: Para leer el archivo Excel de facturas descargado del CRM y transformar los datos hasta obtener el formato requerido por SAP.
- **OpenpyXL**: Para dar formato al archivo final (formato de tabla, agrupación de celdas, etc.).
- **Tkinter**: Para crear una interfaz gráfica de usuario (GUI) con varios botones que facilitan el trabajo a los contables.
- **Auto-py-to-exe**: Para compilar el código y generar un ejecutable (.exe).

### Ejemplo de Uso

1. **Carga del Archivo CRM**: Los usuarios cargan el archivo Excel descargado desde el CRM a través de la interfaz del programa.
2. **Conversión**: Hacen clic en el botón "Convertir" para transformar los datos automáticamente.
3. **Archivo Final**: El programa genera el archivo Excel en el formato correcto para ser cargado en SAP Business One.

### Tecnologías y Herramientas

- **Lenguajes**: Python
- **Librerías**: pandas, numpy, openpyxl, tkinter
- **Herramientas de Desarrollo**: Auto-py-to-exe

### Repositorio del Proyecto

Puedes encontrar el código fuente y más detalles sobre este proyecto en el siguiente enlace:
[Repositorio de Carga Masiva de Facturas en SAP Business One](https://github.com/tu-usuario/carga-masiva-facturas-sap)

---


### Excel extraído del CRM
![Automatización de Tareas](https://github.com/adriansg1991/Automatizaciones/blob/main/1.png)

