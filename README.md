# Proyecto de CRUD para un Inventario de Teclados

Este proyecto es un CRUD (Create, Read, Update, Delete) para un inventario de teclados de una tienda, desarrollado utilizando Python, Flask y las librerías xlwt, xlrd y xlutils.

La aplicación permite llevar un registro actualizado de los teclados disponibles en la tienda, y realizar operaciones CRUD para añadir nuevos teclados, actualizar la información de los teclados existentes y eliminar teclados que ya no se encuentren en el inventario.

## Instalación

Para utilizar la aplicación, es necesario instalar las siguientes librerías de Python:

- Flask
- xlwt
- xlrd
- xlutils

Estas pueden ser instaladas utilizando pip, ejecutando el siguiente comando en una terminal:

pip install flask xlwt xlrd xlutils

## Uso

Para ejecutar la aplicación, es necesario ejecutar el comando `flask run` dentro de la carpeta `xls2web`
Luego de esto, la aplicación estará disponible en el puerto 5000 de la dirección `localhost`.
La aplicación permite visualizar todos los teclados en el inventario, añadir nuevos teclados, actualizar la información de teclados existentes y eliminar teclados.

## Endpoints de API
GET /api/informacion
Devuelve la información de la pagina.

GET /api/productos/
Devuelve una lista de productos y el número total de productos.

GET /api/productos/<int:id>
Devuelve el producto con el ID proporcionado.

GET /api/logo.png
Devuelve el logo de la pagina.

Endpoints de XLS
GET /xls
Devuelve el número de hojas y los nombres de las hojas en el archivo XLS.

GET /xls/<int:sheet>
Devuelve los datos de la hoja especificada por sheet. Se pueden proporcionar los siguientes parámetros opcionales:

- containsCol: Devuelve el nombre de la columna que contiene el valor proporcionado.
- cols: Devuelve las columnas especificadas en una lista separada por comas.
- sortBy: Devuelve los datos de la hoja ordenados por la columna especificada.
- GET /xls/<int:sheet>/<int:col> Devuelve los datos de la columna especificada por col en la hoja especificada por sheet.

GET /xls/<int:sheet>/<int:col>/<int:row>
Devuelve el valor de la celda especificada por col y row en la hoja especificada por sheet.

## Créditos

Este proyecto fue desarrollado por Axel Enciso para una tarea escolar en la materia lenguajes y automatas 2, con el profesor Pakoy3k.
