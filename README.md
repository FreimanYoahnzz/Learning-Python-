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
Usando una analogía simple pensando que es lo mismo que abrir un cuaderno; Esto conlleva una serie de pasos, como:
  1. abrir el cuaderno
  2. Escribir algo nuevo ó leer lo que ya estaba escrito
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

La estructura vista anteriormente vista de una forma general quedaría de la siguiente forma:  

    whith open("PrimerArgumento", "SegundoArgumento") as NombreVariable:
- **with**: Es la palabra clave que abre un bloque administrado, garantiza que algo se "limpie" solo al final(en este caso, hace que el archivo se cierre), 
pase lo que pase adentro, incluso si hay un error.  
- **open(...)**: Es la función que abre el archivo, devuelve un objeto archivo(un objeto especial con métodos como .read(), .write(), etc).
- **PrimerArgumento**: Es la ruta/nombre del archivo(si no se le da una ruta completa, Python lo busca en la carpeta donde corre el script).
- **SegundoArgumento**: Es el modo de apertura.
- **as NombreVariable**: Le da un nombre de variable al objeto archivo que open() devolvió, para usarlo dentro del bloque.

**Modos de apertura**  






