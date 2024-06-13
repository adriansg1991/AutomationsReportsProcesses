# Automatización de Tareas en Departamentos Contables/Financieros

Es cierto que la automatización de tareas en departamentos contables/financieros puede ser muy beneficiosa. La implementación de tecnologías y herramientas automatizadas puede ahorrar tiempo, reducir errores humanos y permitir que los profesionales se centren en tareas más estratégicas y analíticas.

Gracias a haber aprendido a programar en Python, me permite mejorar este tipo de procesos manuales con el objetivo de automatizarlos.

Como he comentado en este post, voy a explicar 3 automatizaciones que he realizado.

## Automatización 1: Informe de Productos Mensual

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
