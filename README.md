# Learning-Python-
Desde fundamentos hasta proyectos backend reales (POO, bases de datos, APIs, automatización).

## Modulo Archivos 
En python, y en programación en general, los archivos sirven para guardar la información de forma permanente
del script que se este realizando, es decir:

Por ejemplo cuando se crea un programa este se ejecuta, y toda la información que se le entregue o este procese
va a vivir solo mientras dicho programa este en ejecución, cuando el programa se cierre, toda la información que 
se halla procesado y guardado se eliminara, ya que dicha ejecución es guardada en la memoria RAM del computador, la cual
guarda todo lo que el programa usa mientras corre, pero se elimina cuando se apaga el computador o se cierra el programa.

Cuando se utilizan archivos esto se guarda directamente en el Disco Duro del computador, permitiendo que los datos persistan
incluso después de que se cierre el programa o se apague el computador. 
Aunque es más lento para leer y escribir(como la información se guarda y no se pierde, se tiene que localizar y mover los datos en un componente distinto),
pero la información persiste, por lo que hace que sea más eficiente y útil en los proyectos.

Para entenderlo mejor podemos ver el proyecto de **ecommerce-carrito**, el cual guarda los datos solo mientras permanece en ejecución el 
proyecto(los datos existen solo en la RAM), cuando se elija la opción de salir del programa, toda la información que contenía se perderá.

**¿Cómo interactúa Python con un archivo?**  
Usando una analogía simple. Es lo mismo que abrir un cuaderno; Esto conlleva una serie de pasos, como:
  1. abrir el cuaderno
  2. Escribir algo nuevo o leer lo que ya estaba escrito
  3. Cerrar el cuaderno

En Python, ese ciclo completo se ve así:  

    archivo = open("notas.txt", "w")  
    archivo.write("Hola mundo")      
    archivo.close()                   
Esta es una forma manual de hacerlo, el problema es que si algo falla en el paso 2 y 3, como algún error inesperado,
el archivo puede quedarse sin cerrar correctamente, corrompiendo los datos.  
Por y para eso existe una estructura más segura para usar:

    with open("notas.txt", "w") as archivo:
      archivo.write("Hola mundo")
Al salir del bloque Python cierra automáticamente el archivo, sin necesidad de llamar a **archivo.close()** manualmente, y se debe de tener en 
cuenta que todo lo que se haga con el archivo(en este caso leer/escribir) debe de ir dentro del bloque(with).  

La estructura vista anteriormente de una forma general quedaría de la siguiente forma:  

    whith open("PrimerArgumento", "SegundoArgumento") as NombreVariable:
- **with**: Es la palabra clave que abre un bloque administrado, garantiza que algo se "limpie" solo al final(en este caso, hace que el archivo se cierre), 
pase lo que pase adentro, incluso si hay un error.  
- **open(...)**: Es la función que abre el archivo, devuelve un objeto archivo(un objeto especial con métodos como .read(), .write(), etc).
- **PrimerArgumento**: Es la ruta/nombre del archivo(si no se le da una ruta completa, Python lo busca en la carpeta donde corre el script).
- **SegundoArgumento**: Es el modo de apertura.
- **as NombreVariable**: Le da un nombre de variable al objeto archivo que open() devolvió, para usarlo dentro del bloque.

### **Modos de apertura**  


|   Modo    | ¿Qué hace? |  Si el archivo NO existe  |  Si el archivo SI existe  |
| --------- | ---------- | ------------------------- | ------------------------- |
|    "r"    | Abre el archivo para leer lo que ya tiene, y no se puede escribir o modificar nada. | Lanza **FileNotFoundError** | Lee desde el principio. |
|    "w"    | Abre el archivo para escribir. | Lo crea | Borra todo el contenido anterior del archivo. |
|    "a"    | Abre el archivo para escribir, pero sin borrar nada, lo que se escriba se suma al final de lo que ya había. | Lo crea | Conserva lo anterior, escribe después. |
|    "x"    | Es como "w", pero Solo si el archivo no existe. | Lo crea | Lanza **FileExistsError** (protección para no sobrescribir sin querer). |
|    "r+"   | Es la combinación de "r" y "w", pero NO borra el contenido anterior del archivo al abrirlo (lectura y escritura). | Lanza error | Lee y escribe sobre el mismo archivo. | 
|    "w+"   | Casi lo mismo que "r+", pero este SI borra el contenido anterior del archivo al abrirlo (escritura y lectura). | Lo crea | Borra todo, después se puede leer/escribir. |
|    "a+"   | Es la combinación de "a" y "r". | Lo crea | Conserva contenido, se puede seguir agregando, y también leer todo el archivo (lo viejo y lo nuevo). |

Agregando una "b" al modo (ej. "rb", "wb") se trabaja en binario (para imágenes, PDFs, ejecutables) en vez de texto.

### **Métodos a usar sobre el objeto archivo**  
|   Método    | ¿Qué hace? | ¿Qué devuelve? |
| --------- | ---------- | ------------------------- |
| .read() | Lee todo el archivo de una vez. | Un solo **string** con todo el contenido. |
| .readlines() | Lee todo el archivo. | Una lista, cada línea es un elemento (con su \n incluido). |
| .write(texto) | Escribe un **string** | No agrega salto de línea solo, hay que ponerle **\n** a mano. |
| .writelines(lista) | Escribe una lista de strings, uno tras otro | Tampoco agrega \n entre elementos automáticamente |  

## Modulo 6: Entornos virtuales
Cada proyecto necesita sus propias librerías, y a veces versiones distintas. Si todo se instala en el Python general del computador, los proyectos se mezclan y uno puede romper a otro. 
Un **entorno virtual** es una carpeta dentro del proyecto (.venv) con su propio Python y sus propias librerías. Es como darle a cada proyecto su propia caja de herramientas,
en vez de una caja compartida donde todo se revuelve.
Este sirve para 3 cosas:
1. Que las librerías de un proyecto no choquen con las de otro.
2. Poder guardar la lista exacta de librerías en un archivo (requirements.txt), para que cualquiera reproduzca tu entorno.
3. Que el computador se mantenga limpio.

**venv** es la abreviatura que viene de virtual environment (entorno virtual), y **.venv** es simplemente el nombre de la carpeta donde vive. El nombre es una convención, y podría llamarse de otra forma.

Los **venv** son como una caja de herramientas por proyecto. Python trae una caja general en el computador, y cada librería que se instala con pip (el sistema de gestión de paquetes oficial de Python) va a esa caja. Con pocos proyectos no se generan inconsistencias, pero con una cantidad elevada de proyectos la cosa cambia.

Supongamos que un proyecto A necesita la librería X en la versión 1, y un proyecto B necesita la versión 2. En la caja general solo cabe una de las dos versiones, y al instalar una la otra no existe, y el otro proyecto se rompería, ya que requiere una versión distinta que el otro.
Con el tiempo la caja general acumula librerías de todos los proyectos, y no no se sabe cuál usa cuál.
Si se quiere que otra persona corra el proyecto, no se sabe qué librerías necesita.
La ventaja de los **venv** es que cada proyecto tiene su propia caja que cumple tres factores claves:
- **Aislamiento:** todo lo que se instale en el proyecto A, solo existira en ese proyecto.
- **Reproducibilidad:** como el entorno solo tiene lo que usa el proyecto, la lista de librerías (requirements.txt) es exacta. Cualquiera crea el entorno y corre el proyecto de igual manera que uno.
- **Limpieza:** si algo se daña, simplemente se borra la carpeta .venv y se recrea en un minuto, sin tocar el Python del computador.

En python, para activar un **venv** simplemente se abre la terminal y estando parado en la carpeta del proyecto, se escribe este comando `.venv\Scripts\Activate.ps1`; para ver las librerías que esta utilizando ese proyecto con el venv se pone `pip list`; para comprobar que de verdad se esta usando el python del entorno se pone `where.exe python`; y para salir del venv, se pone `deactivate`, esto hace que el .venv desaparezca por completo.
Para guardar la lista de librerías que utiliza el venv, se pone `pip freeze > requirements.txt`, esto con el fin de que este pueda ser utilizado de forma correcta en otros computadores.
**requirements.txt** es el nombre del archivo en donde se va a guardar todo (puede ser cualquier nombre, pero el estandar en la industria y que todo el mundo reconoce es el mensionado anteriormente).
**pip freeze** imprime las librerías instaladas en el entorno, cada una con su versión exacta, en el formato **nombre==versión**, el cual se puede ver en el archivo txt.
**>** redirige esa salida, en vez de mostrarla en pantalla, la escribe dentro de un archivo.











