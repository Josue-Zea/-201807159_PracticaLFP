# SimpleQl


SimpleQl es un programa a nivel de consola enfocado en un lenguaje de consultas, de manera que, pueda ingresar multiples registros con archivos externos y poder acceder a ellos con mucha facilidad.

El lenguaje de programación utilizado en este programa es Python en su versión 3.8.4 con el uso del IDE pycharm el cual puede descargar desde el siguiente [enlace](https://www.jetbrains.com/es-es/pycharm/).

> SimpleQl funciona como una versión minimalista
> con algunas similitudes al lenguaje de consultas
> SQL, en su lugar, este permite al usuario cargar 
> información a memoria por medio de comandos y 
> obtener algunos datos  generales acerca de esta.

Para poder hacer uso de esta aplicación únicamente deberá ejecutar el archivo Main en algún programa que tenga soporte para python o desde el mismo pycharm.
# Lista de comandos disponibles:

| Comando | Uso |
| ------ | ------ |
| Cargar | Permite ingresar registros al sistema |
| Seleccionar | Muestra en pantalla los registros solicitados |
| Maximo | Muestra en pantalla el valor máximo de un parámetro |
| Minimo | Muestra en pantalla el valor mínimo de un parámetro |
| Suma | Muestra en pantalla la suma de los valores de un parámetro |
| Cuenta | Muestra en pantalla la cantidad de registros en el sistema |
| Reportar | Genera un reporte en un archivo html |

### Comando: Cargar
Con el uso de este comando podrá cargar al sistema con registros que se encuentren en un archvio .json. Para que el sistema pueda ubicar los archivos debe situarlos en la carpeta que contiene el archivo Main que ejecuta el programa, la estructura del comando es la siguiente:

* Cargar archivo1.json
* Cargar archivo1.json, archivo2.json,..., archivoN.json

Debe colocar el nombre del archivo a ingresar al sistema seguido de la extensión .json, si desea ingresar más de un archivo a la vez debe separarlos por una coma y un espacio (, ).


### Comando: Seleccionar

Con el uso de este comando podrá mostrar en pantalla registros que ya estén cargados en el sistema, puede mostrar ciertos registros y a su vez ciertos parámetros si así lo desea. 
##### Palabras y simbolos del comando :
* " * ": Se utiliza para mostrar en pantalla todos los registros o seleccionar todos los campos.
* "DONDE": Se utiliza cuando busca una cierta condición específica en los registros.

Si desea conocer uno o varios parametros especificamente de los registros basta con colocar el nombre de este parámetro seguido de una busqueda selectiva, es decir, del uso de la palabra DONDE.

Las estructuras que puede utilizar son las siguientes:

| Comando | Explicación |
| ------ | ------ |
| Seleccionar * | Muestra en pantalla todos los registros en el sistema. |
| Seleccionar * donde... | Muestra en pantalla todos los campos de los registros que coincidan en la busqueda. |
|Seleccionar nombre donde...|Muestra en pantalla únicamente el o los campos ingresados que coincidan en la busqueda. |

##### Consideraciones a tomar en cuenta al usar buscqueda selectiva (DONDE):
Debe especificar el parámetro que será la condición a buscar dentro de los registros seguido del simbolo de igualdad "=" seguido del valor a buscar. En el caso de realizar una busqueda por "NOMBRE" este debe ser ingresado dentro de comillas ("") para ser validado por el sistema.
Ejemplos de uso de busqueda selectiva:
```sh
 Seleccionar * Donde Nombre = "Pepito"
```
```sh
 Seleccionar * Donde Edad = 45
```
```sh
 Seleccionar Edad Donde Nombre = "Pepito"
```
```sh
 Seleccionar Edad, Promedio Donde Nombre = "Pepito"
```
### Comando: Maximo

Con el uso de este comando podremos saber el valor máximo numérico que se encuentre en uno de los atributos de los registros existentes en memoria. Únicamente se podrá realizar esto en los atributos Edad y Promedio.
Estructura:
*  Maximo edad
*  Maximo promedio
### Comando: Minimo

Con el uso de este comando podremos saber el valor mínimo numérico que se encuentre en uno de los atributos de los registros existentes en memoria. Únicamente se podrá realizar esto en los atributos Edad y Promedio.
Estructura:
* Minimo edad
* Minimo promedio

### Comando: Suma

Con el uso de este comando podremos saber cual es la sumatoria total de todos los valores de un atributo. Únicamente se podrá realizar esto en los atributos Edad y Promedio.
Estructura:
* Suma edad
* Suma promedio

### Comando: Cuenta
Con el uso de este comando podrás obtener el número total de registros que se hayan ingresado al sistema por medio del comando "CARGAR".
Estructura:
*   Cuenta

### Comando: Reportar
Con el uso de este comando podrás crear un reporte con un determinado número de registros que tú especifíques, el mismo se te mostrará automáticamente en tu navegador y el archivo se creará en la carpeta del programa.
Estructura:
*   Reportar N

### Archivos .json
Para poder cargar registros al sistema es necesario cargarlos en un archivo json con un formato específico que se detalla a continuación, el mismo puede contenter cualquier cantidad de registros media vez cumpla con el formato:
> [
    {
        "nombre": "registro 1",
        "edad": 45,
        "activo": true,
        "promedio": 56.456
    },
    {
        "nombre": "registro 2",
        "edad": 35,
        "activo": false,
        "promedio": 45.896
    }
]

### Nota:
Todos los comandos ingresados en el sistema no diferencian entre mayúsculas y minúsculas, lo que quiere decir que no importa si el comando está escrito totalmente en mayúsculas, minúsculas o intercalados su funcionamiento será el mismo.
