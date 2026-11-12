# Learning-Python-
Desde fundamentos hasta proyectos backend reales (POO, bases de datos, APIs, automatización).

## Índice

- [Modulo Archivos](#modulo-archivos)
- [Modulo 6: Entornos virtuales](#modulo-6-entornos-virtuales)
- [Git y GitHub](#git-y-github)
- [JSON: guardar y leer datos](#json-guardar-y-leer-datos)
- [Manejo de errores aplicado](#manejo-de-errores-aplicado)
- [Buenas prácticas de código](#buenas-prácticas-de-código)
- [Herramientas de Python](#herramientas-de-python)
- [Type hints y mypy](#type-hints-y-mypy)
- [Estilo de código (PEP 8)](#estilo-de-código-pep-8)
- [Decoradores](#decoradores)
- [Bases de datos: SQL, SQLite y Python](#bases-de-datos-sql-sqlite-y-python)
  - [1. Conceptos básicos](#1-conceptos-básicos)
  - [2. Tipos de datos en SQLite](#2-tipos-de-datos-en-sqlite)
  - [3. Crear y modificar tablas (DDL)](#3-crear-y-modificar-tablas-ddl)
  - [4. Insertar, actualizar y borrar (DML)](#4-insertar-actualizar-y-borrar-dml)
  - [5. Consultar con SELECT](#5-consultar-con-select)
  - [6. JOIN: unir tablas](#6-join-unir-tablas)
  - [7. Agregaciones y GROUP BY](#7-agregaciones-y-group-by)
  - [8. Subconsultas, operaciones de conjuntos, CTE y vistas](#8-subconsultas-operaciones-de-conjuntos-cte-y-vistas)
  - [9. Diseño de bases de datos](#9-diseño-de-bases-de-datos)
  - [10. Índices](#10-índices)
  - [11. Transacciones](#11-transacciones)
  - [12. PRAGMA, sqlite_master y la consola de SQLite](#12-pragma-sqlite_master-y-la-consola-de-sqlite)
  - [13. Python con sqlite3](#13-python-con-sqlite3)
  - [14. SQLAlchemy (ORM)](#14-sqlalchemy-orm)
  - [15. NoSQL y otras bases de datos](#15-nosql-y-otras-bases-de-datos)
  - [16. Diferencias entre motores](#16-diferencias-entre-motores)
  - [17. Chuleta: errores y buenas prácticas](#17-chuleta-errores-y-buenas-prácticas)
  - [18. Dónde profundizar](#18-dónde-profundizar)
- [📌 RESUMEN DE CIERRE · Módulo: Bases de datos (SQLite)](#-resumen-de-cierre--módulo-bases-de-datos-sqlite)
  - [1. Python: conceptos nuevos](#1-python-conceptos-nuevos)
  - [2. SQLite: lo que se suma](#2-sqlite-lo-que-se-suma)
  - [3. Patrón de migración de datos](#3-patrón-de-migración-de-datos)
  - [4. Git y GitHub: ramas, pull request y etiquetas](#4-git-y-github-ramas-pull-request-y-etiquetas)
  - [5. Documentar un proyecto](#5-documentar-un-proyecto)
  - [6. Calidad de código](#6-calidad-de-código)
  - [7. Errores comunes de este módulo](#7-errores-comunes-de-este-módulo)

---

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

[⬆ Volver al índice](#índice)


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

[⬆ Volver al índice](#índice)


## Git y GitHub

**Git** es un sistema de control de versiones: guarda "fotos" completas del proyecto (commits) para poder volver atrás, ver qué cambió y trabajar con otros. **GitHub** es el sitio web donde se guarda una copia remota del repositorio.

Una analogía: el proyecto es un libro; cada **commit** es una foto de todas sus páginas en ese momento; la **etiqueta (tag)** es un marcapáginas fijo en una de esas fotos.

### Flujo de trabajo básico

| Comando | ¿Qué hace? |
| ------- | ---------- |
| `git init -b main` | Crea un repositorio nuevo en la carpeta actual, con la rama principal llamada `main`. |
| `git status` | Muestra el estado: archivos en rojo (sin seguimiento o modificados) y en verde (preparados para el próximo commit). |
| `git add archivo1 archivo2` | Pasa archivos al área de preparación (staging), la lista de lo que entrará en el próximo commit. Se pueden poner varios nombres separados por espacio. |
| `git commit -m "mensaje"` | Guarda una foto del proyecto con lo que está preparado. El mensaje dice **qué hace** el cambio. |
| `git log --oneline` | Muestra el historial, un commit por línea (código corto de 7 caracteres + mensaje). |
| `git diff archivo` | Muestra qué cambió en un archivo respecto al último commit (rojo con `-` = quitado, verde con `+` = agregado). |
| `git restore --staged archivo` | Saca un archivo del área de preparación (deshace un `git add`). |
| `git remote add origin URL` | Conecta el repositorio local con el de GitHub (`origin` es el nombre que se le da). |
| `git push -u origin main` | Sube los commits a GitHub. El `-u` se usa solo la primera vez: deja enlazada la rama para que después baste `git push`. |
| `git push` | Sube los commits nuevos. |

**Reglas que se aprendieron:**
- **Un commit por propósito.** Los cambios de estilo van en un commit y las funciones nuevas en otro. Así el historial cuenta una historia clara.
- **Evitar `git add .`** al inicio: agrega todo lo que haya, y es la forma en que se cuelan archivos que no deben subirse. Mejor escribir los nombres.
- **Revisar el punto de "sin guardar"** (●) en la pestaña del editor antes de hacer commit: Git solo ve lo que está guardado en disco.

### Qué significan `HEAD`, `main` y el código del commit

- **Código del commit** (por ejemplo `b81b6ab`): el identificador corto de esa foto.
- **`HEAD`**: "tú estás aquí", el commit en el que está parado el proyecto.
- **`main`**: nombre de la rama principal; es una etiqueta **móvil** que avanza con cada commit.
- **`origin/main`**: la copia de `main` que está en GitHub. Si `main` y `origin/main` apuntan al mismo commit, están sincronizados.

### Etiquetas (tags) y versiones

Una etiqueta **no contiene cambios**: solo **señala un commit** y se queda quieta. La versión siguiente se marca sobre un commit nuevo, que incluye todo lo anterior porque el historial es acumulativo.

| Comando | ¿Qué hace? |
| ------- | ---------- |
| `git tag -a v0.1 -m "mensaje"` | Crea una etiqueta anotada sobre el commit actual. |
| `git tag` | Lista las etiquetas. |
| `git push origin v0.1` | Sube la etiqueta a GitHub (un `git push` normal **no** sube etiquetas). |

### `.gitignore`

Archivo en la raíz del proyecto con lo que Git debe **ignorar**: una regla por línea. El comodín `*` significa "cualquier cosa".

```
.venv/
__pycache__/
*.pyc
.env
datos.json
registro_*.json
.mypy_cache/
```

Regla: el **código** va al repositorio; los **datos que genera el programa**, las caches y el entorno virtual no. Los secretos (`.env`) nunca.

[⬆ Volver al índice](#índice)


---

## JSON: guardar y leer datos

**JSON** es un formato de texto para guardar datos con estructura (diccionarios, listas, textos, números). Python lo maneja con el módulo `json`.

**La regla para no confundirse:** `dump` y `load` trabajan con un **archivo**; `dumps` y `loads` (la **s** es de *string*) trabajan con **texto**.

| Función | ¿Qué hace? | ¿Qué devuelve? |
| ------- | ---------- | -------------- |
| `json.dump(datos, f, indent=2)` | Escribe los datos **en el archivo** `f`. | `None` (solo escribe). |
| `json.load(f)` | Lee el archivo `f` y lo convierte en datos de Python. | Un diccionario (o lista). |
| `json.dumps(datos, ensure_ascii=False)` | Convierte los datos **en un texto**. No toca ningún archivo. | Un `str`. |
| `json.loads(texto)` | Convierte un texto JSON en datos de Python. | Un diccionario (o lista). |

Opciones útiles: `indent=2` guarda el JSON con sangría, legible; `ensure_ascii=False` conserva tildes y signos (`¡`, `ñ`) en vez de convertirlos a códigos como `¡`.

```python
import json

# Guardar un diccionario en un archivo
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2)

# Leer el archivo y recuperar el diccionario
with open("datos.json", "r", encoding="utf-8") as f:
    datos = json.load(f)
```

Siempre se abre el archivo con `encoding="utf-8"` para que las tildes y las `ñ` no se dañen.

### Modos de archivo que más se usan con JSON

| Modo | Para qué | Si el archivo NO existe |
| ---- | -------- | ----------------------- |
| `"r"` | Leer (con `json.load`). | `FileNotFoundError` |
| `"w"` | Escribir y **borrar** lo anterior (con `json.dump`). | Lo crea |
| `"a"` | Escribir **al final**, sin borrar lo anterior. | Lo crea |

### JSON Lines (`.jsonl`): un registro por línea

Un archivo donde **cada línea es un JSON independiente**. Sirve para registros que crecen sin parar, porque solo se **agrega** una línea al final con el modo `"a"`, sin leer ni reescribir todo, y una línea dañada no se lleva el resto.

```python
# Agregar un registro (el "\n" salta de línea; sin él los registros quedan pegados)
with open("registros.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(registro, ensure_ascii=False) + "\n")

# Leer todos los registros, saltando las líneas dañadas
registros = []
with open("registros.jsonl", "r", encoding="utf-8") as f:
    for linea in f:            # recorrer un archivo da una línea por vuelta
        try:
            registros.append(json.loads(linea))
        except json.JSONDecodeError:
            pass                # línea dañada: se salta y se sigue con la siguiente
```

[⬆ Volver al índice](#índice)


---

## Manejo de errores aplicado

| Error | ¿Cuándo aparece? |
| ----- | ---------------- |
| `FileNotFoundError` | Abrir en modo `"r"` un archivo que no existe. |
| `json.JSONDecodeError` | El contenido del archivo no es un JSON válido (por ejemplo, está dañado). |
| `FileExistsError` | Abrir con modo `"x"` un archivo que ya existe. |
| `TypeError` | Una función recibió un tipo que no esperaba (por ejemplo, `None` donde iba un texto). |
| `NameError` | Se usó un nombre (variable, función, módulo) que no existe o no se importó. |

- Un `try` puede tener **varios `except`**, cada uno para un error distinto.
- **Dónde poner el `try`:** si va **fuera** de un `for`, el primer error corta todo el bucle. Si va **dentro**, solo falla esa vuelta y el bucle continúa.
- `pass` = "no hacer nada" en ese `except`. Úsalo solo cuando ignorar el error es una decisión consciente.

**Cómo leer un traceback (el mensaje de error largo):** empieza por la **última línea** (el tipo de error y qué pasó) y sube: cada bloque dice el archivo y la línea donde ocurrió.

**Patrón: archivo dañado sin perder datos.** En vez de borrar el archivo roto, se mueve a otro nombre y se crea uno nuevo:

```python
except json.JSONDecodeError:
    shutil.move("datos.json", "datos_danado.json")   # el archivo roto se conserva
    datos = crear_datos_por_defecto()                # se crea uno nuevo
```

Para no pisar un archivo dañado anterior, se busca el primer número libre con un `while` y `os.path.exists`:

```python
numero = 1
nombre = f"datos_danado_{numero}.json"
while os.path.exists(nombre):
    numero += 1
    nombre = f"datos_danado_{numero}.json"
```

[⬆ Volver al índice](#índice)


---

## Buenas prácticas de código

- **Una sola responsabilidad por función y por módulo.** Cada pieza hace una cosa.
- **Separar la lógica de la interfaz.** Las funciones que procesan datos no llevan `print` ni `input`: reciben datos y devuelven datos. Solo una parte del programa habla con el usuario. Así la interfaz (consola, web, ventana) se puede cambiar sin tocar la lógica.
- **DRY (*Don't Repeat Yourself*):** si un valor se escribe en varios lugares, va en **una constante**. Si se equivoca una letra en una constante, Python avisa con `NameError`; si se equivoca en un texto repetido a mano, no avisa nada y el error queda escondido.
- **Constantes en MAYÚSCULAS** (`NOMBRE_ARCHIVO`), variables y funciones en `snake_case`.
- **Un módulo no ejecuta código suelto al importarse.** Todo lo que corre va dentro de una función `main()`, y al final del archivo:

```python
if __name__ == "__main__":
    main()
```

Esto significa "ejecuta `main()` solo si ejecuto este archivo directamente, no si alguien lo importa".

### Dos nombres para el mismo objeto (aliasing)

```python
a = {"nombre": ""}
b = a            # NO copia: son dos nombres para el MISMO diccionario
b["nombre"] = "Ana"
print(a)         # {'nombre': 'Ana'}
```

Para obtener una copia independiente, incluso con diccionarios dentro de diccionarios, se usa `copy.deepcopy(objeto)` (el módulo `copy` viene con Python). `.copy()` solo copia el primer nivel.

### `return` frente a efecto secundario

- Una función que **devuelve** un valor termina con `return valor`.
- Una función que solo **hace algo** (escribir en un archivo, imprimir) devuelve `None`.
- **Error típico:** guardar en una variable lo que devuelve una función que no devuelve nada (`x = guardar(m)`): `x` vale `None`.
- Un `return` **dentro** de un `while` o `for` corta la función en ese instante; un `return` **después** del bucle solo corre cuando el bucle termina solo.

[⬆ Volver al índice](#índice)


---

## Herramientas de Python

### Texto

| Herramienta | ¿Qué hace? | Ejemplo |
| ----------- | ---------- | ------- |
| `texto.lower()` | Devuelve el texto en minúsculas (los textos no se modifican: **hay que guardar el resultado**). | `"HOLA".lower()` → `"hola"` |
| `texto.strip()` | Quita espacios al inicio y al final. | `"  hola ".strip()` → `"hola"` |
| `texto.split()` | Sin argumentos: parte el texto en palabras, separando por cualquier cantidad de espacios y descartando vacíos. | `" a   b ".split()` → `["a", "b"]` |
| `" ".join(lista)` | Une los elementos de una lista de textos con un espacio entre cada uno. | `" ".join(["a", "b"])` → `"a b"` |
| `letra.isalnum()` | `True` si es letra o número (incluye letras con tilde). | `"é".isalnum()` → `True` |
| f-string | Inserta variables dentro de un texto con `{...}`. Solo se usa la `f` cuando hay `{}`. | `f"Hola {nombre}"` |
| `+=` con textos | Pega al final: sirve para ir acumulando un resultado. | `r = ""` ; `r += "a"` |

### Patrón del "colador y el balde" (acumular un resultado)

1. Crear el "balde" **antes** del bucle (`resultado = ""` o `resultado = []`).
2. Dentro del bucle, filtrar con un `if` y **agregar** lo que sirve (`+=` o `.append(...)`).
3. Devolver el balde **después** del bucle.

```python
def solo_digitos(texto):
    resultado = ""
    for letra in texto:
        if letra.isdigit():
            resultado += letra
    return resultado
```

### Quitar tildes (módulo `unicodedata`)

`unicodedata.normalize("NFD", texto)` separa cada letra con tilde en **letra base + marca**; `unicodedata.combining(c)` devuelve un número distinto de 0 si `c` es una marca. Quedarse solo con los caracteres cuyo `combining` es 0 deja el texto sin tildes.

```python
import unicodedata

def quitar_tildes(texto):
    resultado = ""
    for letra in unicodedata.normalize("NFD", texto):
        if unicodedata.combining(letra) == 0:
            resultado += letra
    return resultado
```

### Buscar una frase como palabra completa dentro de un texto

Comparar con `in` solo encuentra la frase aunque esté metida dentro de otra palabra (`"oe" in "joe"` es `True`). Para evitarlo:

1. Normalizar el texto: minúsculas, sin tildes, sin puntuación, con un solo espacio entre palabras.
2. Ponerle un espacio al inicio y al final: `f" {texto} "`.
3. Buscar la frase también rodeada de espacios: `f" {frase} " in texto_limpio`.

Así `" oe "` no coincide dentro de `"joe"`, y las frases de varias palabras (`"hasta luego"`) se encuentran completas. **Las frases que se buscan deben estar ya normalizadas** (minúsculas y sin tildes), si no, nunca coinciden.

### Diccionarios y bucles

```python
# Recorrer un diccionario: clave y valor a la vez
for categoria, lista in DICCIONARIO.items():
    for elemento in lista:
        ...
```

Un diccionario dentro de otro se lee con un par de corchetes por nivel: `datos["usuario"]["nombre"]`.

### Condiciones y flujo

| Herramienta | ¿Qué hace? |
| ----------- | ---------- |
| `if nombre:` / `if not nombre:` | Un texto vacío (`""`) o una lista vacía (`[]`) cuentan como "falso"; con contenido, como "verdadero". |
| `x in lista` / `x not in lista` | Pregunta si un elemento está (o no) en la lista; también `"hola" in "hola, buenas"` para textos. |
| `while True:` | Bucle que repite para siempre hasta un `break` o un `return`. |
| `break` | Corta el bucle en ese instante. |
| `continue` | Salta al inicio de la siguiente vuelta sin ejecutar el resto. |
| `input("texto")` | Muestra el texto, espera a que el usuario escriba y devuelve lo escrito como `str`. |

### Archivos y sistema

| Herramienta | ¿Qué hace? |
| ----------- | ---------- |
| `os.path.exists(ruta)` | `True` si el archivo o carpeta existe, `False` si no. |
| `shutil.move(origen, destino)` | Mueve un archivo; si el destino está en la misma carpeta con otro nombre, lo **renombra**. Crea el destino si no existe. |
| `datetime.now().isoformat(timespec="seconds")` | La fecha y hora actual como texto: `"2026-10-22T08:26:31"` (con `from datetime import datetime`). |
| `copy.deepcopy(obj)` | Copia independiente de un objeto, a todos los niveles. |

[⬆ Volver al índice](#índice)


---

## Type hints y mypy

Los **type hints** son anotaciones que indican qué tipo de dato recibe y devuelve una función. Python **no las obliga** al ejecutar; sirven para documentar y para que herramientas revisen el código sin ejecutarlo.

```python
def saludar(nombre: str) -> str:
    return f"Hola {nombre}"

def guardar(datos: dict) -> None:   # no devuelve nada -> None
    ...

def main() -> None:                 # sin parámetros: paréntesis vacíos
    ...
```

**Reglas:**
- Toda función lleva su retorno anotado. Si no devuelve nada, `-> None`.
- Una función sin parámetros no lleva nada entre los paréntesis, pero su retorno sí se anota.
- Tipos comunes: `str`, `int`, `float`, `bool`, `list`, `dict`; más específicos: `list[str]` (lista de textos), `dict[str, list[str]]`.

### `mypy`

Librería que revisa los tipos de todo el proyecto **sin ejecutarlo**.

```
pip install mypy        # con el entorno virtual activo
mypy archivo.py         # revisar un archivo
mypy .                  # revisar todo el proyecto
```

| Mensaje de `mypy` | Significado |
| ----------------- | ----------- |
| `Success: no issues found in 5 source files` | Éxito: no se encontraron problemas en 5 archivos. |
| `Missing return statement [return]` | Falta la instrucción `return` en una función que dice devolver algo. |
| `Incompatible return value type (got "str", expected "dict")` | El valor devuelto es de un tipo incompatible: devolvió un `str` pero se esperaba un `dict`. |
| `Argument 1 has incompatible type "int"; expected "str"` | El argumento 1 es de tipo `int` pero se esperaba `str`. |
| `... does not return a value` | Esa función no devuelve ningún valor (se está usando su resultado). |

Con `-> dict` en una función que olvidó el `return`, `mypy` detecta al instante el bug de que devuelva `None`.

**Después de instalar o quitar una librería:** `pip freeze > requirements.txt` actualiza la lista (`pip freeze` imprime las librerías instaladas con su versión exacta, `nombre==versión`; `>` escribe esa salida dentro del archivo en vez de mostrarla en pantalla).

[⬆ Volver al índice](#índice)


---

## Estilo de código (PEP 8)

- 4 espacios por nivel de sangría; consistente dentro de cada bloque.
- **Dos** líneas en blanco entre funciones y entre una constante y el primer `def`.
- En argumentos con nombre, sin espacios alrededor del `=`: `encoding="utf-8"`.
- Sin espacios sobrantes al final de las líneas ni líneas vacías de más al final del archivo.
- Nombres que dicen lo que guardan: `texto_sin_tildes`, no `letras_tilde`.

[⬆ Volver al índice](#índice)


## Decoradores

Una **función es un objeto** más en Python: se puede guardar en una variable, pasar como argumento a otra función y devolver desde una función. Un **decorador** usa eso: es una función que **recibe una función** y **devuelve una versión nueva** que hace algo extra antes o después de la original, sin tocar su código. Como envolver un regalo: el regalo es el mismo, pero lo envuelves.

```python
def anunciar(funcion):
    def envoltura(*args, **kwargs):
        print(f"Llamando a {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print("Listo")
        return resultado
    return envoltura


@anunciar
def sumar(a, b):
    return a + b


print(sumar(2, 3))   # imprime "Llamando a sumar", "Listo" y luego 5
```

### Las piezas

| Pieza | ¿Qué es / qué hace? |
| ----- | ------------------- |
| `@anunciar` encima de la función | Atajo para `sumar = anunciar(sumar)`: el nombre `sumar` pasa a apuntar a la versión envuelta. |
| `envoltura` | La función nueva: hace el trabajo extra y en medio llama a la original. |
| `*args, **kwargs` | Captura cualquier argumento (posicionales y con nombre) y los reenvía tal cual a la original, para que el decorador sirva con cualquier función. |
| `return resultado` (dentro de la envoltura) | Devuelve lo que devolvió la original. **Si se olvida, la función decorada devuelve `None`** y todo lo que dependa de ella se rompe. |
| `return envoltura` (al final, **sin paréntesis**) | El decorador entrega la función nueva sin ejecutarla. Con paréntesis (`envoltura()`) la ejecutaría. |
| `funcion.__name__` | El nombre de la función, como texto (`"sumar"`). Va sin paréntesis porque es un dato guardado en la función. |
| `@wraps(funcion)` (de `functools`) | Va encima de `envoltura`; hace que la función decorada conserve su nombre y su documentación originales. Sin él, `__name__` valdría `"envoltura"`. |

La envoltura **recuerda** el valor de `funcion` aunque el decorador ya haya terminado de ejecutarse. Esto se llama *closure* y es lo que hace funcionar el truco.

### Ejemplo útil: medir cuánto tarda una función

```python
import time
from functools import wraps

DEPURACION = True


def medir_tiempo(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        milisegundos = (time.perf_counter() - inicio) * 1000
        if DEPURACION:
            print(f"[{funcion.__name__}] {milisegundos:.2f} ms")
        return resultado
    return envoltura
```

- **`time.perf_counter()`** no da la hora del día: es un **cronómetro** de alta precisión que devuelve segundos desde un punto cero arbitrario. Solo tiene sentido **restar dos lecturas** (inicio y fin). Para la hora real, `datetime.now()`.
- **`* 1000`** pasa de segundos a milisegundos (1 s = 1000 ms).
- **`DEPURACION`** es una bandera: el decorador es una herramienta de diagnóstico que se apaga (`False`) cuando el programa se publica. Para eso, más adelante, se usa el módulo `logging` en lugar de `print`.
- Un decorador que vive en un módulo aparte (`utilidades.py`) se puede reutilizar en cualquier otro: `from utilidades import medir_tiempo` y `@medir_tiempo` encima de la función.

### Formato dentro de un f-string

Lo que va después de los dos puntos le dice a Python cómo mostrar el valor.

| Formato | Resultado | Ejemplo |
| ------- | --------- | ------- |
| `{x:.2f}` | Número decimal con 2 decimales | `f"{3.14159:.2f}"` → `"3.14"` |
| `{x:.0f}` | Sin decimales (redondea) | `f"{2.7:.0f}"` → `"3"` |

### Para qué más sirven los decoradores

Registrar errores, comprobar permisos, guardar resultados en caché, reintentar una llamada que falla, y marcar rutas en una API (`@app.get("/ruta")`).

### Aviso sobre los type hints

Anotar tipos en un decorador requiere herramientas más avanzadas (`Callable`, `ParamSpec`); por ahora se dejan sin anotar. `mypy` no se queja por eso.

### Código suelto en un módulo importado

Si un archivo que se va a importar (como `utilidades.py`) tiene código de prueba suelto (por ejemplo un `print(...)` al final), ese código **se ejecuta cada vez que alguien lo importa**. Las pruebas se borran o se dejan dentro de `if __name__ == "__main__":`.

[⬆ Volver al índice](#índice)


# Bases de datos: SQL, SQLite y Python

Referencia del módulo. Los ejemplos se probaron con SQLite 3.45. Cuando una función exige una versión reciente de SQLite, se indica junto a ella.

Contenido:

1. [Conceptos básicos](#1-conceptos-básicos)
2. [Tipos de datos en SQLite](#2-tipos-de-datos-en-sqlite)
3. [Crear y modificar tablas (DDL)](#3-crear-y-modificar-tablas-ddl)
4. [Insertar, actualizar y borrar (DML)](#4-insertar-actualizar-y-borrar-dml)
5. [Consultar con SELECT](#5-consultar-con-select)
6. [JOIN: unir tablas](#6-join-unir-tablas)
7. [Agregaciones y GROUP BY](#7-agregaciones-y-group-by)
8. [Subconsultas, operaciones de conjuntos, CTE y vistas](#8-subconsultas-operaciones-de-conjuntos-cte-y-vistas)
9. [Diseño de bases de datos](#9-diseño-de-bases-de-datos)
10. [Índices](#10-índices)
11. [Transacciones](#11-transacciones)
12. [PRAGMA, sqlite_master y la consola de SQLite](#12-pragma-sqlite_master-y-la-consola-de-sqlite)
13. [Python con sqlite3](#13-python-con-sqlite3)
14. [SQLAlchemy (ORM)](#14-sqlalchemy-orm)
15. [NoSQL y otras bases de datos](#15-nosql-y-otras-bases-de-datos)
16. [Diferencias entre motores](#16-diferencias-entre-motores)
17. [Chuleta: errores y buenas prácticas](#17-chuleta-errores-y-buenas-prácticas)
18. [Dónde profundizar](#18-dónde-profundizar)

---

## 1. Conceptos básicos

- **Base de datos:** conjunto organizado de datos guardados para consultarlos y modificarlos de forma rápida y segura.
- **Base de datos relacional:** guarda los datos en **tablas**. Cada **fila** es un registro y cada **columna** es un campo. Las tablas se relacionan entre sí mediante **claves**.
- **SGBD (sistema gestor):** el programa que administra la base de datos (SQLite, PostgreSQL, SQL Server, MySQL).
- **SQL:** el lenguaje para hablar con una base relacional. Es un estándar, pero cada motor tiene sus variantes (dialectos).

| Motor | Cómo funciona | Cuándo se usa |
| ----- | ------------- | ------------- |
| SQLite | Un solo archivo (`.db`), sin servidor, viene con Python | Aprender, prototipos, apps pequeñas y móviles |
| PostgreSQL | Servidor aparte, gratuito y muy completo | Aplicaciones web y proyectos serios |
| SQL Server | Servidor de Microsoft | Ecosistema .NET / C# |
| MySQL / MariaDB | Servidor, muy extendido en web | Sitios web, hosting compartido |

### Tipos de sentencias SQL

| Familia | Sentencias | Para qué |
| ------- | ---------- | -------- |
| DDL (definición) | `CREATE`, `ALTER`, `DROP` | Crear o cambiar la estructura |
| DML (manipulación) | `INSERT`, `UPDATE`, `DELETE` | Cambiar los datos |
| DQL (consulta) | `SELECT` | Leer datos |
| TCL (transacciones) | `BEGIN`, `COMMIT`, `ROLLBACK` | Agrupar cambios en bloques |
| DCL (permisos) | `GRANT`, `REVOKE` | Permisos de usuarios (no existe en SQLite) |

### Reglas de escritura

- Cada sentencia termina en `;`.
- Comentarios: `-- hasta el final de la línea` y `/* varias líneas */`.
- Los **textos** van entre comillas simples: `'MENSUAL'`. Las comillas dobles son para nombres de tablas o columnas con caracteres raros.
- Las palabras clave no distinguen mayúsculas (`select` = `SELECT`). La convención es escribirlas en mayúsculas y los nombres de tablas y columnas en minúsculas con guion bajo (`fecha_vencimiento`).
- En SQLite, comparar texto con `=` **sí distingue mayúsculas**: `'a' = 'A'` es falso. `LIKE` no las distingue (con letras ASCII). Con `COLLATE NOCASE` se ignoran las mayúsculas: `WHERE nombre = 'ana' COLLATE NOCASE`.

[⬆ Volver al índice](#índice)


---

## 2. Tipos de datos en SQLite

SQLite guarda cinco clases de valores:

| Clase | Qué es |
| ----- | ------ |
| `NULL` | Sin valor |
| `INTEGER` | Entero |
| `REAL` | Decimal (coma flotante) |
| `TEXT` | Texto |
| `BLOB` | Datos binarios tal cual (imágenes, archivos) |

- Los tipos declarados (`INT`, `VARCHAR(50)`, `DATE`...) solo dan una *afinidad*: una sugerencia. **SQLite es flexible**: en una columna `INTEGER` puede entrar un texto sin quejarse. Para que valide los tipos, se crea la tabla como `STRICT` (SQLite 3.37 o posterior): `CREATE TABLE t (a INTEGER, b TEXT) STRICT;`.
- **No existe el tipo booleano.** Se usa `INTEGER` con `0` (falso) y `1` (verdadero).
- **No existe el tipo fecha.** Se guardan como texto ISO: `'2026-10-28'` o `'2026-10-28 14:30:00'`. Así se ordenan y se comparan bien como texto. También se admiten enteros (tiempo Unix) o reales (día juliano).
- **Dinero:** `REAL` puede producir errores de redondeo. En proyectos reales se guarda en la unidad mínima como entero (centavos) o se usa `NUMERIC` en motores que lo soportan (PostgreSQL).
- `typeof(valor)` devuelve la clase de un valor: `SELECT typeof(1), typeof('a'), typeof(1.5), typeof(NULL);`.
- `CAST(valor AS INTEGER)` convierte entre tipos.

### NULL

`NULL` significa "no hay valor" o "se desconoce". No es `0` ni `''` (texto vacío).

- `= NULL` **nunca** da verdadero. Se pregunta con `IS NULL` / `IS NOT NULL`.
- Cualquier operación con `NULL` da `NULL`: `5 + NULL` es `NULL`.
- Las funciones de agregación ignoran los `NULL` (salvo `COUNT(*)`).

[⬆ Volver al índice](#índice)


---

## 3. Crear y modificar tablas (DDL)

```sql
CREATE TABLE IF NOT EXISTS planes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    precio REAL NOT NULL CHECK (precio > 0),
    duracion_dias INTEGER
);

CREATE TABLE IF NOT EXISTS socios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT,
    plan_id INTEGER REFERENCES planes(id) ON DELETE SET NULL,
    fecha_inicio TEXT,
    fecha_vencimiento TEXT,
    activo INTEGER NOT NULL DEFAULT 1
);
```

Estructura: `CREATE TABLE nombre ( columna tipo restricciones, ... );`. El **nombre va antes del tipo**, las columnas se separan con comas y la última no lleva coma.

### Restricciones (constraints)

| Restricción | Qué hace |
| ----------- | -------- |
| `PRIMARY KEY` | Identificador único de cada fila (no se repite ni es `NULL`) |
| `NOT NULL` | La columna es obligatoria |
| `UNIQUE` | No permite valores repetidos |
| `DEFAULT valor` | Valor que se pone si no se indica ninguno |
| `CHECK (condición)` | El valor debe cumplir la condición |
| `REFERENCES tabla(columna)` | Clave foránea: el valor debe existir en esa otra tabla |

- `INTEGER PRIMARY KEY` (exactamente `INTEGER`) se **llena solo**: SQLite asigna el mayor `id` existente + 1. Con `INT PRIMARY KEY` no pasa eso. `AUTOINCREMENT` evita que se reutilicen `id` de filas borradas, pero casi nunca hace falta.
- Clave primaria **compuesta** (varias columnas): `PRIMARY KEY (socio_id, clase_id)` al final de la tabla.
- `UNIQUE` en varias columnas: `UNIQUE (nombre, fecha)`.
- Una clave foránea también se puede escribir al final de la tabla: `FOREIGN KEY (plan_id) REFERENCES planes(id)`. Es lo mismo.
- El tipo de la clave foránea debe coincidir con el de la columna a la que apunta.

### Qué pasa al borrar o cambiar el registro referenciado

Se indica con `ON DELETE` y `ON UPDATE`:

| Acción | Efecto |
| ------ | ------ |
| `NO ACTION` / `RESTRICT` | Impide borrar si hay filas que dependen de él (es el comportamiento normal) |
| `CASCADE` | Borra (o actualiza) también las filas dependientes |
| `SET NULL` | Pone `NULL` en la clave foránea de las filas dependientes |
| `SET DEFAULT` | Pone el valor por defecto |

**SQLite no revisa las claves foráneas a menos que se active** con `PRAGMA foreign_keys = ON;` en **cada conexión**. DB Browser lo activa por defecto; en Python hay que hacerlo tú.

### Borrar y modificar la estructura

```sql
DROP TABLE IF EXISTS socios;   -- primero la tabla que depende...
DROP TABLE IF EXISTS planes;   -- ...y después la referenciada

ALTER TABLE socios ADD COLUMN correo TEXT;
ALTER TABLE socios RENAME COLUMN correo TO email;   -- SQLite 3.25 o posterior
ALTER TABLE socios DROP COLUMN email;               -- SQLite 3.35 o posterior
ALTER TABLE socios RENAME TO miembros;
```

- `IF NOT EXISTS` / `IF EXISTS` evitan el error al crear algo que ya existe o borrar algo que no existe. Un script con `DROP TABLE IF EXISTS` al inicio se puede ejecutar completo las veces que quieras.
- Cambiar el tipo o las restricciones de una columna existente no se puede con `ALTER` en SQLite: se crea una tabla nueva, se copian los datos y se borra la vieja.

[⬆ Volver al índice](#índice)


---

## 4. Insertar, actualizar y borrar (DML)

### INSERT

```sql
INSERT INTO planes (nombre, precio, duracion_dias) VALUES ('MENSUAL', 100000, 31);

-- varias filas en una sola sentencia
INSERT INTO planes (nombre, precio, duracion_dias)
VALUES ('TRIMESTRAL', 278999, 95),
       ('ANUAL', 999999, 365);

-- copiar desde un SELECT
INSERT INTO socios_archivo (nombre) SELECT nombre FROM socios WHERE activo = 0;
```

- Los valores van **por posición**: el primer valor corresponde a la primera columna de la lista, y así sucesivamente.
- Todas las filas de un mismo `INSERT` llevan **las mismas columnas**. Si una columna no se nombra, toma su `DEFAULT` o `NULL`.
- Para dejar un campo sin dato, escribe `NULL` (sin comillas), no `''`.
- Ejecutar dos veces el mismo `INSERT` **duplica** las filas, salvo que haya un `UNIQUE` que lo impida.

Variantes para choques con `UNIQUE` o clave primaria:

```sql
INSERT OR IGNORE INTO planes (nombre, precio) VALUES ('MENSUAL', 1);      -- si existe, lo ignora
INSERT OR REPLACE INTO planes (id, nombre, precio) VALUES (1, 'MENSUAL', 1);  -- borra y reinserta

-- upsert (SQLite 3.24 o posterior): insertar o, si existe, actualizar
INSERT INTO planes (nombre, precio) VALUES ('MENSUAL', 120000)
ON CONFLICT(nombre) DO UPDATE SET precio = excluded.precio;

-- devolver el id generado (SQLite 3.35 o posterior)
INSERT INTO planes (nombre, precio) VALUES ('ANUAL', 999999) RETURNING id;
```

### UPDATE

```sql
UPDATE socios
SET plan_id = 1, fecha_inicio = '2026-10-26', fecha_vencimiento = '2026-11-26'
WHERE id = 8;

UPDATE productos SET stock = stock - 1 WHERE id = 3;   -- usa el valor actual
```

### DELETE

```sql
DELETE FROM socios WHERE id = 6;
DELETE FROM socios;          -- vacía la tabla (la tabla sigue existiendo)
```

### La regla de oro

**Un `UPDATE` o un `DELETE` sin `WHERE` afecta todas las filas.** Antes de ejecutarlos, escribe un `SELECT` con el **mismo `WHERE`** y comprueba qué filas devuelve. Después de ejecutarlos, el resultado dice cuántas filas afectó (`N rows affected`): si no coincide con lo esperado, algo está mal.

| Sentencia | Qué hace |
| --------- | -------- |
| `DELETE FROM t` | Borra los datos, la tabla queda |
| `DROP TABLE t` | Borra la tabla completa (estructura y datos) |
| `TRUNCATE` | No existe en SQLite (en otros motores vacía la tabla rápido) |

[⬆ Volver al índice](#índice)


---

## 5. Consultar con SELECT

### 5.1 Orden de escritura y orden de ejecución

Se escribe en este orden y **cada parte aparece una sola vez**:

```sql
SELECT   columnas
FROM     tabla
JOIN     otra tabla ON regla
WHERE    filtro de filas
GROUP BY columnas de agrupación
HAVING   filtro de grupos
ORDER BY orden
LIMIT    cantidad OFFSET saltar;
```

SQL **ejecuta** en otro orden, y por eso el `WHERE` va después del `JOIN` y el `HAVING` después del `GROUP BY`:

1. `FROM` y `JOIN`: arma la tabla de trabajo.
2. `WHERE`: descarta filas.
3. `GROUP BY`: forma las pilas.
4. `HAVING`: descarta pilas.
5. `SELECT`: calcula las columnas que se muestran.
6. `DISTINCT`, `ORDER BY` y `LIMIT`.

### 5.2 Columnas

```sql
SELECT * FROM socios;                                  -- todas las columnas
SELECT nombre, telefono FROM socios;                   -- solo algunas
SELECT nombre AS socio, precio * 12 AS anual FROM planes;   -- alias y cálculos
SELECT DISTINCT plan_id FROM socios;                   -- sin repetidos
```

- `AS` solo cambia el nombre en el resultado, no en la tabla.
- Evita `SELECT *` en código real: pide solo las columnas que necesitas.

### 5.3 WHERE: filtros

| Operador | Significado |
| -------- | ----------- |
| `=`, `!=` o `<>` | Igual, distinto |
| `<`, `>`, `<=`, `>=` | Comparaciones |
| `AND`, `OR`, `NOT` | Combinar condiciones |
| `IN (1, 2, 3)` / `NOT IN (...)` | Está (o no) en una lista |
| `BETWEEN a AND b` | Entre a y b, **incluyendo** ambos extremos |
| `LIKE 'patrón'` | Búsqueda por patrón en texto |
| `IS NULL` / `IS NOT NULL` | Sin valor / con valor |

- `AND` se evalúa antes que `OR`. Cuando mezcles ambos, usa paréntesis: `WHERE activo = 1 AND (plan_id = 1 OR plan_id = 2)`.
- `WHERE telefono = NULL` **nunca** devuelve filas. Usa `IS NULL`.

### 5.4 Patrones con LIKE y GLOB

| Patrón | Significado |
| ------ | ----------- |
| `'J%'` | Empieza por J |
| `'%A'` | Termina en A |
| `'%an%'` | Contiene "an" |
| `'J_AN'` | `_` es exactamente un carácter cualquiera |

- `%` es "cualquier cantidad de caracteres" (también ninguno).
- `LIKE` ignora mayúsculas y minúsculas (con letras ASCII).
- `GLOB` es como `LIKE` pero distingue mayúsculas y usa `*` y `?`: `nombre GLOB 'J*'`.
- Para buscar un `%` literal: `LIKE '50\%' ESCAPE '\'`.

### 5.5 ORDER BY, LIMIT y OFFSET

```sql
SELECT nombre FROM socios ORDER BY nombre ASC;                          -- A a Z (ASC es el valor por defecto)
SELECT nombre FROM socios ORDER BY fecha_vencimiento DESC, nombre ASC;  -- varios criterios (el 2.º desempata)
SELECT nombre FROM socios ORDER BY fecha_vencimiento LIMIT 3;           -- los 3 primeros
SELECT nombre FROM socios ORDER BY nombre LIMIT 10 OFFSET 20;           -- paginación: salta 20 y trae 10
```

- Sin `ORDER BY`, el orden de las filas **no está garantizado**.
- Paginación: `OFFSET = (página - 1) * tamaño_de_página`.
- En SQLite los `NULL` se ordenan como el valor más pequeño (primero en `ASC`). Se puede cambiar con `NULLS LAST` / `NULLS FIRST` (3.30 o posterior).

### 5.6 Condicionales y valores nulos

```sql
SELECT nombre,
       CASE
           WHEN fecha_vencimiento < '2026-10-28' THEN 'vencido'
           WHEN fecha_vencimiento < '2026-11-28' THEN 'por vencer'
           ELSE 'vigente'
       END AS estado
FROM socios;

SELECT COALESCE(telefono, 'sin teléfono') FROM socios;   -- primer valor que no sea NULL
SELECT IFNULL(telefono, 'sin teléfono') FROM socios;     -- igual, con dos argumentos
SELECT NULLIF(telefono, '') FROM socios;                 -- devuelve NULL si es igual al segundo valor
```

### 5.7 Funciones frecuentes

| Texto | Qué hace |
| ----- | -------- |
| `a \|\| b` | Concatena |
| `LENGTH(t)` | Cantidad de caracteres |
| `UPPER(t)`, `LOWER(t)` | Mayúsculas, minúsculas |
| `TRIM(t)`, `LTRIM(t)`, `RTRIM(t)` | Quita espacios |
| `SUBSTR(t, inicio, largo)` | Fragmento (el primer carácter es la posición 1) |
| `REPLACE(t, buscar, nuevo)` | Reemplaza |
| `INSTR(t, buscar)` | Posición de un texto dentro de otro (0 si no está) |

| Números | Qué hace |
| ------- | -------- |
| `ROUND(x, n)` | Redondea a n decimales |
| `ABS(x)` | Valor absoluto |
| `MAX(a, b)`, `MIN(a, b)` | Con 2 o más argumentos, el mayor o menor de ellos |
| `RANDOM()` | Entero aleatorio |

| Fechas | Qué hace |
| ------ | -------- |
| `date('now')` | Fecha de hoy (en UTC) |
| `datetime('now', 'localtime')` | Fecha y hora locales |
| `date('2026-10-26', '+31 days')` | Suma días: `2026-11-26` |
| `date('2026-10-26', '-1 month')`, `'start of month'` | Otros modificadores |
| `strftime('%Y-%m', fecha)` | Da formato: `%Y` año, `%m` mes, `%d` día, `%H:%M:%S` hora |
| `julianday(f2) - julianday(f1)` | Días entre dos fechas |

Cuidado con las fechas inexistentes: `date('2026-11-31')` devuelve en silencio `2026-12-01` (noviembre tiene 30 días). Python, en cambio, lanza `ValueError`. Los meses con 31 días son enero, marzo, mayo, julio, agosto, octubre y diciembre.

[⬆ Volver al índice](#índice)


---

## 6. JOIN: unir tablas

Una **clave foránea** guarda solo un número (`plan_id = 3`). `JOIN` junta dos tablas **fila por fila** cuando se cumple una regla, y así puedes ver los datos completos (el nombre del plan, no solo su número).

```sql
SELECT s.nombre AS socio, p.nombre AS plan, p.precio
FROM socios AS s
INNER JOIN planes AS p ON p.id = s.plan_id
WHERE s.activo = 1
ORDER BY s.nombre;
```

- `FROM socios AS s`: la tabla principal, con el apodo `s`.
- `INNER JOIN planes AS p`: la segunda tabla, con el apodo `p`.
- `ON p.id = s.plan_id`: la regla de emparejamiento (clave primaria = clave foránea). Sin ella no se sabe qué fila va con cuál.
- `s.nombre` se lee "la columna `nombre` de la tabla `s`". Es **obligatorio** cuando dos tablas tienen una columna con el mismo nombre (si no, `ambiguous column name`). Es buena costumbre ponerlo siempre.
- El `WHERE` y el `ORDER BY` van **después** del `JOIN`.

### Tipos de JOIN

| JOIN | Qué devuelve |
| ---- | ------------ |
| `INNER JOIN` | Solo las filas que **encuentran pareja** en la otra tabla |
| `LEFT JOIN` | **Todas** las filas de la tabla del `FROM`; si no hay pareja, las columnas de la otra salen en `NULL` |
| `RIGHT JOIN` | Lo contrario de `LEFT` (SQLite 3.39 o posterior) |
| `FULL OUTER JOIN` | Todas las filas de ambos lados (SQLite 3.39 o posterior) |
| `CROSS JOIN` | Todas las combinaciones posibles (producto cartesiano); se usa poco |

- **¿Cuál es la tabla principal?** Aquella de la que quieres una fila en el resultado. "Lista de socios con su plan" → `FROM socios`. "Cada plan con sus socios, incluso los planes sin socios" → `FROM planes LEFT JOIN socios`. Con `INNER` el orden no cambia el resultado; con `LEFT` sí.
- **Encontrar los que no tienen pareja** (muy usado):

```sql
SELECT s.nombre
FROM socios AS s
LEFT JOIN planes AS p ON p.id = s.plan_id
WHERE p.id IS NULL;      -- socios sin plan válido
```

- **Trampa:** si usas un `LEFT JOIN` y filtras en el `WHERE` una columna de la tabla de la derecha (`WHERE p.precio > 0`), las filas sin pareja (con `NULL`) se eliminan y el `LEFT` se comporta como `INNER`. Para filtrar solo la tabla de la derecha sin perder filas, pon la condición en el `ON`.
- **Varios JOIN:** se encadenan: `FROM a JOIN b ON ... JOIN c ON ...`.
- **Auto-join:** una tabla unida consigo misma (por ejemplo empleados y su jefe, que también es empleado), con dos apodos distintos.

[⬆ Volver al índice](#índice)


---

## 7. Agregaciones y GROUP BY

Una **función de agregación** toma muchas filas y devuelve **un solo valor**.

| Función | Devuelve |
| ------- | -------- |
| `COUNT(*)` | Cuántas **filas** hay |
| `COUNT(columna)` | Cuántas filas tienen valor (no `NULL`) en esa columna |
| `COUNT(DISTINCT columna)` | Cuántos valores distintos hay |
| `SUM(columna)` | La suma (da `NULL` si no hay filas) |
| `TOTAL(columna)` | La suma, pero da `0.0` si no hay filas |
| `AVG(columna)` | El promedio |
| `MIN(columna)` / `MAX(columna)` | El menor / el mayor |
| `GROUP_CONCAT(columna, ', ')` | Une los valores en un solo texto |

`COUNT(*)` no apunta a ninguna columna: cuenta filas. Con esta tabla:

| nombre | telefono |
| ------ | -------- |
| ANA | 3001112222 |
| LUIS | NULL |
| SOFIA | 3003334444 |
| CARLOS | NULL |

`COUNT(*)` da 4 y `COUNT(telefono)` da 2. `SUM(*)` no existe: `SUM` necesita una columna con números.

### GROUP BY: cálculo por pila

Sin `GROUP BY` la función calcula sobre **todas** las filas como si fueran una sola pila. `GROUP BY` hace dos pasos:

1. **Reparte** las filas en pilas, según el valor de la columna indicada.
2. **Ejecuta la función una vez por pila**, y devuelve **una fila por pila**.

```sql
SELECT p.nombre AS plan, COUNT(*) AS cantidad, SUM(p.precio) AS total
FROM socios AS s
INNER JOIN planes AS p ON p.id = s.plan_id
WHERE s.activo = 1
GROUP BY p.nombre;
```

| plan | cantidad | total |
| ---- | -------- | ----- |
| MENSUAL | 2 | 200000 |
| TRIMESTRAL | 1 | 278999 |
| ANUAL | 1 | 999999 |

Reglas:

- En el `SELECT` solo pueden ir **la columna (o columnas) del `GROUP BY` y funciones de agregación**. Una columna suelta que no sea ninguna de esas no tiene sentido (SQLite no da error, pero devuelve un valor cualquiera de la pila: es engañoso).
- Agrupa **solo** por lo que identifica la pila. Columnas de más parten las pilas en más pilas.
- Se puede agrupar por varias columnas: `GROUP BY p.nombre, s.activo` (una pila por cada combinación).

### WHERE vs HAVING

- `WHERE` filtra **filas**, **antes** de agrupar.
- `HAVING` filtra **pilas**, **después** de calcular, y se usa con funciones de agregación.

```sql
SELECT plan_id, COUNT(*) AS cantidad
FROM socios
WHERE activo = 1
GROUP BY plan_id
HAVING COUNT(*) >= 2;
```

### Total general y desglose juntos

El total general es **otra pila** (la de todos), no cabe como columna de una consulta agrupada. Se resuelve con dos consultas o con una de estas técnicas:

```sql
-- 1) Fila extra de total al final, con UNION ALL (ambos SELECT con el mismo número de columnas)
SELECT p.nombre, COUNT(*), SUM(p.precio)
FROM socios AS s INNER JOIN planes AS p ON p.id = s.plan_id
WHERE s.activo = 1
GROUP BY p.nombre
UNION ALL
SELECT 'TOTAL', COUNT(*), SUM(p.precio)
FROM socios AS s INNER JOIN planes AS p ON p.id = s.plan_id
WHERE s.activo = 1;

-- 2) Función de ventana (SQLite 3.25 o posterior): el total repetido en cada fila
SELECT p.nombre, SUM(p.precio) AS total_plan,
       SUM(SUM(p.precio)) OVER () AS total_general
FROM socios AS s INNER JOIN planes AS p ON p.id = s.plan_id
WHERE s.activo = 1
GROUP BY p.nombre;
```

[⬆ Volver al índice](#índice)


---

## 8. Subconsultas, operaciones de conjuntos, CTE y vistas

### Subconsultas

Un `SELECT` dentro de otro, entre paréntesis.

```sql
-- en el WHERE, con IN
SELECT nombre FROM socios
WHERE plan_id IN (SELECT id FROM planes WHERE precio > 200000);

-- valor único (subconsulta escalar)
SELECT nombre FROM planes WHERE precio > (SELECT AVG(precio) FROM planes);

-- EXISTS: ¿hay al menos una fila relacionada?
SELECT nombre FROM planes AS p
WHERE EXISTS (SELECT 1 FROM socios AS s WHERE s.plan_id = p.id);

-- en el FROM, como tabla temporal
SELECT AVG(cantidad) FROM (SELECT COUNT(*) AS cantidad FROM socios GROUP BY plan_id);
```

Cuidado: `x NOT IN (subconsulta)` no devuelve **ninguna fila** si la subconsulta contiene algún `NULL`. Con `NOT EXISTS` no pasa.

### Operaciones de conjuntos

Unen los resultados de dos `SELECT` con el mismo número de columnas, en el mismo orden:

| Operador | Resultado |
| -------- | --------- |
| `UNION ALL` | Todas las filas de ambos, con repetidas |
| `UNION` | Igual, pero quita las repetidas |
| `INTERSECT` | Solo las filas que están en los dos |
| `EXCEPT` | Las del primero que no están en el segundo |

### CTE (WITH)

Da un nombre a una consulta intermedia para que la principal sea más legible:

```sql
WITH por_plan AS (
    SELECT plan_id, COUNT(*) AS n
    FROM socios
    GROUP BY plan_id
)
SELECT p.nombre, pp.n
FROM por_plan AS pp
INNER JOIN planes AS p ON p.id = pp.plan_id;
```

### Vistas

Una consulta guardada con nombre, que se usa como si fuera una tabla (no guarda datos propios):

```sql
CREATE VIEW socios_activos AS
SELECT id, nombre, plan_id FROM socios WHERE activo = 1;

SELECT * FROM socios_activos;
DROP VIEW socios_activos;
```

### Funciones de ventana (adelanto)

Calculan sobre un grupo de filas **sin colapsarlas** en una sola (SQLite 3.25 o posterior):

```sql
SELECT nombre, fecha_vencimiento,
       ROW_NUMBER() OVER (ORDER BY fecha_vencimiento) AS posicion,
       COUNT(*) OVER (PARTITION BY plan_id) AS socios_del_plan
FROM socios;
```

Otras: `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, `SUM() OVER (...)`.

[⬆ Volver al índice](#índice)


---

## 9. Diseño de bases de datos

### Claves

| Clave | Qué es |
| ----- | ------ |
| Primaria (PK) | Identifica cada fila de forma única. Una por tabla |
| Foránea (FK) | Columna que apunta a la PK de otra tabla; crea la relación |
| Natural | Un dato real que identifica (cédula, correo). Puede cambiar o repetirse |
| Sustituta | Un número inventado (`id`). Es lo más recomendable como PK |

### Tipos de relación

| Relación | Ejemplo | Cómo se implementa |
| -------- | ------- | ------------------ |
| Uno a uno (1:1) | Usuario y su perfil | FK con `UNIQUE` en una de las dos tablas |
| Uno a muchos (1:N) | Un plan, muchos socios | La FK va en el lado de los **muchos** (`socios.plan_id`) |
| Muchos a muchos (N:M) | Socios y clases (un socio va a varias clases; una clase tiene varios socios) | **Tabla intermedia** con dos FK |

```sql
CREATE TABLE inscripciones (
    socio_id INTEGER NOT NULL REFERENCES socios(id) ON DELETE CASCADE,
    clase_id INTEGER NOT NULL REFERENCES clases(id) ON DELETE CASCADE,
    fecha TEXT NOT NULL,
    PRIMARY KEY (socio_id, clase_id)
);
```

### Normalización

Es ordenar las tablas para no repetir datos y evitar inconsistencias.

- **1.ª forma normal:** cada celda guarda **un solo valor** (no listas ni "campos repetidos"). Mal: una columna `intenciones` con `'saludar, despedirse'`. Bien: una fila por valor, en otra tabla relacionada.
- **2.ª forma normal:** si la clave es compuesta, cada columna depende de **toda** la clave, no de una parte.
- **3.ª forma normal:** las columnas dependen **solo de la clave primaria**, no de otra columna. Mal: guardar en `socios` el `plan_nombre` y el `plan_precio` junto al `plan_id` (el precio depende del plan). Bien: el precio vive en `planes`.

Ventaja: si el precio de un plan cambia, se actualiza **una sola fila**, no 200. A veces se **desnormaliza a propósito** (repetir un dato) para ganar velocidad o guardar un histórico (el precio que se pagó ese día).

### Modelo entidad-relación (ER)

Es el plano antes de construir: **entidades** (futuras tablas), **atributos** (columnas) y **relaciones** con su cardinalidad (1:N, N:M). Herramientas para dibujarlo: dbdiagram.io, draw.io y DBeaver (genera el diagrama desde una base ya creada).

### Convenciones y checklist

- Nombres en minúsculas con guion bajo, sin tildes ni espacios. Elige plural o singular para las tablas y mantenlo en todo el proyecto.
- La FK se llama `tabla_id` (`plan_id`). Cada tabla lleva su `id`.
- Guarda las fechas en formato ISO. Usa `NOT NULL` en lo obligatorio, `UNIQUE` en lo que no se debe repetir y `CHECK` para reglas simples.
- Antes de crear una tabla, pregúntate: ¿qué entidad es?, ¿cuál es su identificador?, ¿qué relaciones tiene?, ¿hay datos repetidos que deberían estar en otra tabla?

[⬆ Volver al índice](#índice)


---

## 10. Índices

Un índice es como el índice de un libro: permite encontrar filas sin leer toda la tabla.

```sql
CREATE INDEX idx_socios_vencimiento ON socios(fecha_vencimiento);
CREATE UNIQUE INDEX idx_socios_telefono ON socios(telefono);
CREATE INDEX idx_socios_plan_activo ON socios(plan_id, activo);   -- compuesto: el orden importa
DROP INDEX idx_socios_vencimiento;
```

- `PRIMARY KEY` y `UNIQUE` ya crean un índice automáticamente.
- Conviene indexar las columnas que se usan mucho en `WHERE`, `JOIN` (las claves foráneas) y `ORDER BY`.
- Costo: ocupan espacio y hacen más lentos los `INSERT`, `UPDATE` y `DELETE`. No indexes todo.
- Un índice compuesto `(a, b)` sirve para buscar por `a` o por `a` y `b`, pero no solo por `b`.
- No ayudan: `LIKE '%texto'` (comodín al inicio) ni aplicar una función a la columna (`WHERE date(fecha) = ...`).
- Para comprobar si se usa: `EXPLAIN QUERY PLAN SELECT ...;`. `SEARCH ... USING INDEX` es bueno; `SCAN tabla` significa que lee toda la tabla.

[⬆ Volver al índice](#índice)


---

## 11. Transacciones

Una **transacción** agrupa varias operaciones en un bloque de "todo o nada". Ejemplo: transferir dinero = restar en una cuenta + sumar en otra. Si falla la segunda, la primera debe deshacerse.

```sql
BEGIN;
UPDATE cuentas SET saldo = saldo - 50000 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 50000 WHERE id = 2;
COMMIT;      -- confirma y guarda
-- ROLLBACK; -- en vez de COMMIT: deshace todo desde el BEGIN
```

Propiedades **ACID**:

| Letra | Significado |
| ----- | ----------- |
| Atomicidad | Todo el bloque se hace o nada se hace |
| Consistencia | Los datos siguen cumpliendo las reglas (claves, `CHECK`...) |
| Aislamiento (Isolation) | Las transacciones simultáneas no se estorban |
| Durabilidad | Lo confirmado no se pierde |

- En **DB Browser**, los cambios quedan pendientes hasta **Write Changes** (`Ctrl+S`). **Revert Changes** descarta lo pendiente.
- SQLite permite **un solo escritor a la vez**: si otra conexión está escribiendo, aparece `database is locked`.
- `SAVEPOINT nombre` / `ROLLBACK TO nombre` permiten puntos de retorno dentro de una transacción.

[⬆ Volver al índice](#índice)


---

## 12. PRAGMA, sqlite_master y la consola de SQLite

```sql
PRAGMA foreign_keys = ON;            -- activar claves foráneas (por conexión)
PRAGMA table_info(socios);           -- columnas, tipos, PK
PRAGMA foreign_key_list(socios);     -- claves foráneas
PRAGMA index_list(socios);           -- índices
PRAGMA journal_mode = WAL;           -- modo que mejora la concurrencia lectura/escritura

SELECT name, sql FROM sqlite_master WHERE type = 'table';   -- catálogo de la base
```

Consola `sqlite3` (se abre con `sqlite3 gimnasio.db`):

| Comando | Qué hace |
| ------- | -------- |
| `.tables` | Lista las tablas |
| `.schema socios` | Muestra el `CREATE TABLE` |
| `.headers on` y `.mode column` | Resultados con encabezados y en columnas |
| `.read script.sql` | Ejecuta un archivo `.sql` |
| `.quit` | Salir |

Atajos de DB Browser for SQLite: `Ctrl+Enter` ejecuta todo (o solo lo seleccionado), `Shift+F5` ejecuta la línea actual, `Ctrl+T` abre una pestaña SQL nueva, `Ctrl+S` guarda los cambios en la base (Write Changes).

[⬆ Volver al índice](#índice)


---

## 13. Python con sqlite3

Es parte de la librería estándar de Python (no se instala nada).

### Flujo básico

```python
import sqlite3

conexion = sqlite3.connect("gimnasio.db")      # abre o crea el archivo (":memory:" = en memoria)
conexion.execute("PRAGMA foreign_keys = ON")
conexion.row_factory = sqlite3.Row             # filas accesibles por nombre de columna

cursor = conexion.execute("SELECT id, nombre FROM socios WHERE activo = ?", (1,))
for fila in cursor.fetchall():
    print(fila["id"], fila["nombre"])

conexion.close()
```

| Pieza | Para qué sirve |
| ----- | -------------- |
| `sqlite3.connect(ruta)` | Abre la conexión a la base |
| `conexion.execute(sql, parámetros)` | Ejecuta una sentencia y devuelve un cursor |
| `conexion.executemany(sql, lista)` | La misma sentencia con muchas filas de parámetros |
| `conexion.executescript(texto)` | Ejecuta varias sentencias seguidas (sin parámetros) |
| `cursor.fetchone()` | La siguiente fila, o `None` si no hay |
| `cursor.fetchall()` | Todas las filas, en una lista |
| `cursor.fetchmany(n)` | Hasta `n` filas |
| `for fila in cursor` | Recorre las filas una a una |
| `cursor.lastrowid` | El `id` de la última fila insertada |
| `cursor.rowcount` | Cuántas filas afectó un `INSERT`, `UPDATE` o `DELETE` |
| `conexion.commit()` | Confirma los cambios |
| `conexion.rollback()` | Descarta los cambios pendientes |
| `conexion.close()` | Cierra la conexión |
| `sqlite3.Row` | Fila con acceso por nombre (`fila["nombre"]`) y `dict(fila)` |

### Parámetros: nunca con f-strings

```python
# MAL: permite inyección SQL (si nombre = "x'; DROP TABLE socios; --" borra la tabla)
conexion.execute(f"SELECT * FROM socios WHERE nombre = '{nombre}'")

# BIEN: el motor trata el valor como dato, nunca como código
conexion.execute("SELECT * FROM socios WHERE nombre = ?", (nombre,))
conexion.execute("SELECT * FROM socios WHERE nombre = :nombre", {"nombre": nombre})
```

- Los parámetros van en una **tupla** (con una coma si es uno: `(valor,)`) o en un diccionario con `:nombre`.
- Solo se pueden parametrizar **valores**, no nombres de tablas o columnas.
- Para buscar con `LIKE`, el patrón completo es el parámetro: `("%" + texto + "%",)`.

### Transacciones en Python

- Por defecto, `sqlite3` abre una transacción automáticamente antes de `INSERT`, `UPDATE` y `DELETE`. Los cambios **no se guardan hasta `commit()`**.
- `with conexion:` hace `commit()` si el bloque termina bien y `rollback()` si hay una excepción. **No cierra la conexión.**
- Para cerrarla siempre: `contextlib.closing`.

```python
from contextlib import closing

with closing(sqlite3.connect("gimnasio.db")) as conexion:
    with conexion:                                   # transacción
        conexion.execute("UPDATE socios SET activo = 0 WHERE id = ?", (6,))
```

### Errores

Todos heredan de `sqlite3.Error`.

| Excepción | Cuándo ocurre |
| --------- | ------------- |
| `sqlite3.IntegrityError` | Se violó `UNIQUE`, `NOT NULL`, `CHECK` o una clave foránea |
| `sqlite3.OperationalError` | SQL mal escrito, tabla o columna inexistente, base bloqueada |
| `sqlite3.ProgrammingError` | Cantidad de parámetros incorrecta, conexión cerrada |
| `sqlite3.DatabaseError` | Error general de la base |

### Fechas

Guárdalas como texto ISO: `datetime.now().isoformat(timespec="seconds")` da `'2026-10-31T23:05:09'`. Python 3.12 desaconsejó los adaptadores automáticos de fechas, así que conviértelas tú mismo.

### Ejemplo: módulo de acceso a datos

```python
import sqlite3
from contextlib import closing
from datetime import datetime

NOMBRE_BD = "gimnasio.db"


def conectar(ruta: str = NOMBRE_BD) -> sqlite3.Connection:
    conexion = sqlite3.connect(ruta)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def crear_tablas(conexion: sqlite3.Connection) -> None:
    with conexion:
        conexion.executescript(
            """
            CREATE TABLE IF NOT EXISTS planes (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL UNIQUE,
                precio REAL NOT NULL
            );
            CREATE TABLE IF NOT EXISTS socios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                plan_id INTEGER REFERENCES planes(id),
                creado_en TEXT NOT NULL
            );
            """
        )


def agregar_plan(conexion: sqlite3.Connection, nombre: str, precio: float) -> int | None:
    with conexion:
        cursor = conexion.execute(
            "INSERT INTO planes (nombre, precio) VALUES (?, ?)",
            (nombre, precio),
        )
    return cursor.lastrowid


def agregar_socio(conexion: sqlite3.Connection, nombre: str, plan_id: int | None) -> int | None:
    ahora = datetime.now().isoformat(timespec="seconds")
    with conexion:
        cursor = conexion.execute(
            "INSERT INTO socios (nombre, plan_id, creado_en) VALUES (?, ?, ?)",
            (nombre, plan_id, ahora),
        )
    return cursor.lastrowid


def buscar_socios(conexion: sqlite3.Connection, texto: str) -> list[sqlite3.Row]:
    cursor = conexion.execute(
        "SELECT id, nombre FROM socios WHERE nombre LIKE ? ORDER BY nombre",
        (f"%{texto}%",),
    )
    return cursor.fetchall()


def socios_por_plan(conexion: sqlite3.Connection) -> list[sqlite3.Row]:
    cursor = conexion.execute(
        """
        SELECT p.nombre AS plan, COUNT(*) AS cantidad
        FROM socios AS s
        INNER JOIN planes AS p ON p.id = s.plan_id
        GROUP BY p.nombre
        ORDER BY cantidad DESC
        """
    )
    return cursor.fetchall()


if __name__ == "__main__":
    with closing(conectar(":memory:")) as conexion:
        crear_tablas(conexion)
        mensual = agregar_plan(conexion, "MENSUAL", 100000)
        agregar_socio(conexion, "ANA", mensual)
        for fila in socios_por_plan(conexion):
            print(dict(fila))
```

Ideas de este ejemplo: la lógica de acceso a datos vive en funciones propias (no mezcladas con `print` ni `input`), cada función usa parámetros `?`, y la conexión se abre en un solo lugar.

Para una aplicación web, usa una conexión por petición (no compartas una conexión entre hilos).

[⬆ Volver al índice](#índice)


---

## 14. SQLAlchemy (ORM)

SQLAlchemy es una librería que traduce entre **tablas y clases de Python**: cada tabla es una clase, cada fila es un objeto. Se instala con `pip install sqlalchemy`.

- **ORM** (mapeo objeto-relacional): trabajas con objetos y la librería genera el SQL.
- **Core:** la parte que arma SQL con funciones de Python, sin clases.
- La gran ventaja: **el motor se cambia con una sola línea** (la cadena de conexión). El mismo código sirve para SQLite en desarrollo y PostgreSQL en producción.

| Motor | Cadena de conexión (ejemplo) |
| ----- | ---------------------------- |
| SQLite | `sqlite:///gimnasio.db` |
| PostgreSQL | `postgresql+psycopg://usuario:clave@localhost/gimnasio` |
| SQL Server | `mssql+pyodbc://usuario:clave@servidor/gimnasio?driver=...` |

```python
from typing import Optional

from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Plan(Base):
    __tablename__ = "planes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(unique=True)
    precio: Mapped[float]
    socios: Mapped[list["Socio"]] = relationship(back_populates="plan")


class Socio(Base):
    __tablename__ = "socios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str]
    plan_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planes.id"))
    plan: Mapped[Optional["Plan"]] = relationship(back_populates="socios")


engine = create_engine("sqlite:///gimnasio.db")
Base.metadata.create_all(engine)          # crea las tablas que falten

with Session(engine) as session:
    mensual = Plan(nombre="MENSUAL", precio=100000)
    session.add(mensual)
    session.add(Socio(nombre="ANA", plan=mensual))
    session.commit()

    consulta = select(Socio).where(Socio.nombre == "ANA")
    ana = session.scalars(consulta).first()
    print(ana.plan.nombre)
```

| Concepto | Qué es |
| -------- | ------ |
| `Engine` | La conexión a la base (se crea una vez) |
| `Session` | Una transacción de trabajo: acumula cambios y los guarda con `commit()` |
| `session.add()` | Agrega un objeto para guardarlo |
| `select(Clase).where(...)` | Arma una consulta |
| `relationship()` | Navega entre objetos relacionados (`ana.plan`) |
| Alembic | Herramienta de **migraciones**: versiona los cambios en la estructura de la base |

Cuándo usarlo: proyectos web o con muchas tablas. Para scripts pequeños, `sqlite3` es más simple. Conviene entender SQL antes, porque el ORM lo genera por ti y necesitas saber qué está pasando.

[⬆ Volver al índice](#índice)


---

## 15. NoSQL y otras bases de datos

"NoSQL" agrupa bases que **no usan tablas relacionales** como modelo principal.

| Tipo | Idea | Ejemplos | Uso típico |
| ---- | ---- | -------- | ---------- |
| Documentos | Guarda documentos tipo JSON | MongoDB | Datos con estructura variable |
| Clave-valor | Un diccionario gigante y rapidísimo | Redis | Caché, sesiones, colas |
| Grafos | Nodos y relaciones | Neo4j | Redes sociales, recomendaciones |
| Columnas anchas | Tablas distribuidas enormes | Cassandra | Volúmenes muy grandes |
| Vectoriales | Guardan vectores (embeddings) y buscan por similitud | pgvector, Chroma, FAISS | Búsqueda semántica y memoria para modelos de lenguaje |

- Relacional: estructura fija, integridad fuerte, transacciones y consultas complejas con `JOIN`. Es la opción por defecto.
- NoSQL: flexibilidad y escala horizontal, a cambio de menos garantías. Muchos proyectos usan varias a la vez (PostgreSQL + Redis).

[⬆ Volver al índice](#índice)


---

## 16. Diferencias entre motores

| Tema | SQLite | PostgreSQL | SQL Server |
| ---- | ------ | ---------- | ---------- |
| `id` automático | `INTEGER PRIMARY KEY` | `GENERATED ALWAYS AS IDENTITY` (o `SERIAL`) | `IDENTITY(1,1)` |
| Limitar filas | `LIMIT n` | `LIMIT n` | `TOP n` o `OFFSET ... FETCH` |
| Concatenar texto | `a \|\| b` | `a \|\| b` | `a + b` o `CONCAT()` |
| Booleano | No hay (0/1) | `BOOLEAN` | `BIT` |
| Fecha de ahora | `datetime('now')` | `NOW()` | `GETDATE()` |
| Tipos | Flexibles (a menos que sea `STRICT`) | Estrictos | Estrictos |
| `LIKE` sin mayúsculas | Por defecto | `ILIKE` | Depende de la configuración (collation) |
| Entrecomillar nombres | `"nombre"` | `"nombre"` | `[nombre]` |
| Acceso | Archivo local | Servidor con usuarios | Servidor con usuarios |

[⬆ Volver al índice](#índice)


---

## 17. Chuleta: errores y buenas prácticas

### Errores frecuentes

| Error | Causa y solución |
| ----- | ---------------- |
| `UPDATE` o `DELETE` sin `WHERE` | Afecta todas las filas. Haz antes un `SELECT` con el mismo `WHERE` |
| `WHERE campo = NULL` | Nunca da verdadero. Usa `IS NULL` |
| Texto vacío `''` en lugar de `NULL` | `IS NULL` no lo encuentra. Usa `NULL` para "sin dato" |
| Fechas con `/` o en formato día/mes/año | No se ordenan ni comparan bien. Usa `AAAA-MM-DD` |
| Fechas inexistentes (`2026-11-31`) | SQLite las "corrige" en silencio. Revisa los días del mes |
| Volver a ejecutar un `INSERT` | Duplica filas. Usa `UNIQUE` o `INSERT OR IGNORE` |
| Olvidar `commit()` en Python | Los cambios se pierden al cerrar la conexión |
| Olvidar `PRAGMA foreign_keys = ON` | SQLite no valida las claves foráneas |
| `WHERE` antes del `JOIN`, o `FROM` antes del `SELECT` | Orden fijo: `SELECT`, `FROM`, `JOIN`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT` |
| Columna suelta junto a una agregación | Debe estar en el `GROUP BY` |
| `HAVING` usado como `WHERE` | `WHERE` filtra filas, `HAVING` filtra grupos |
| Armar SQL con f-strings | Inyección SQL. Usa parámetros `?` |
| Dos tablas con el mismo apodo | Cada tabla necesita un apodo propio |
| Filtrar la tabla derecha de un `LEFT JOIN` en el `WHERE` | Elimina las filas sin pareja. Pon la condición en el `ON` |

### Mensajes de error de SQLite

| Mensaje | Qué significa |
| ------- | ------------- |
| `near "X": syntax error` | Error de escritura cerca de `X` (casi siempre algo anterior: falta una coma, o una parte está en mal orden) |
| `no such table: t` / `no such column: c` | La tabla o columna no existe (revisa el nombre y los apodos) |
| `table t already exists` | Ya existe: usa `IF NOT EXISTS` o `DROP TABLE IF EXISTS` |
| `ambiguous column name: nombre` | Dos tablas tienen esa columna: usa el prefijo `s.nombre` |
| `UNIQUE constraint failed: tabla.columna` | Valor repetido en una columna `UNIQUE` o clave primaria |
| `NOT NULL constraint failed: tabla.columna` | Falta un dato obligatorio |
| `FOREIGN KEY constraint failed` | La clave apunta a una fila que no existe (o se intenta borrar una fila de la que otras dependen) |
| `CHECK constraint failed` | El valor no cumple la regla `CHECK` |
| `N values for M columns` | Las filas de `VALUES` no tienen tantos valores como columnas hay en la lista |
| `SELECTs to the left and right of UNION ALL do not have the same number of result columns` | Los dos `SELECT` deben tener el mismo número de columnas |
| `database is locked` | Otra conexión está escribiendo (o hay cambios sin guardar en DB Browser) |
| `Incorrect number of bindings supplied` (Python) | Hay más o menos parámetros que signos `?` |

### Buenas prácticas

- Guarda tu estructura y datos de práctica en un archivo `.sql` que se pueda ejecutar completo desde cero (con `DROP TABLE IF EXISTS` al inicio).
- Escribe un comentario encima de cada consulta que diga qué hace, y que coincida con lo que hace el código.
- Usa apodos cortos y prefija todas las columnas (`s.nombre`) cuando hay más de una tabla.
- Prueba cada consulta por separado antes de combinarla con otras.
- Pide solo las columnas que necesitas y filtra en la base, no en Python.
- Los datos de práctica que subas a un repositorio público deben ser inventados (nada de teléfonos o nombres reales).

[⬆ Volver al índice](#índice)


---

## 18. Dónde profundizar

- Documentación de SQLite: https://www.sqlite.org/lang.html (lenguaje SQL), https://www.sqlite.org/datatype3.html (tipos) y https://www.sqlite.org/lang_datefunc.html (fechas).
- Módulo `sqlite3` de Python: https://docs.python.org/3/library/sqlite3.html
- SQLAlchemy: https://docs.sqlalchemy.org
- Práctica de SQL interactiva: https://sqlbolt.com y https://sqlzoo.net

[⬆ Volver al índice](#índice)



---

# 📌 RESUMEN DE CIERRE · Módulo: Bases de datos (SQLite)

> [!IMPORTANT]
> Este bloque cierra el módulo de bases de datos. Reúne lo nuevo que apareció al aplicar SQLite en un proyecto real: herramientas de Python, comandos de Git y errores comunes. Los resúmenes de cierre de los demás módulos tendrán este mismo formato.

## 1. Python: conceptos nuevos

### `try` / `finally`: ejecutar algo SIEMPRE
El bloque `finally` se ejecuta haya error, `return` o Ctrl+C. Se usa para cerrar recursos.
```python
conexion = sqlite3.connect("app.db")   # se abre ANTES del try
try:
    ...                                 # trabajo con la base de datos
finally:
    conexion.close()                    # se cierra siempre
```
- Si `connect()` estuviera dentro del `try` y fallara, el `finally` intentaría cerrar una variable que no existe y taparía el error real.
- `with conexion:` **no cierra** la conexión: solo confirma (`commit`) o revierte (`rollback`) la transacción.

### Parámetros con valor por defecto
```python
def guardar(dato: str, fecha: str | None = None) -> None:
    if fecha is None:
        fecha = datetime.now().isoformat(timespec="seconds")
```
- Los parámetros con valor por defecto van **al final**.
- `str | None` significa "texto o `None`". `None` se usa como "no me lo dieron".
- El valor por defecto solo se usa si **no pasas el argumento**. Si escribes `fecha=d["fecha"]` y la clave no existe, falla antes de llamar a la función.

### Diccionarios: `[]` vs `.get()`
| Forma | Si la clave no existe |
|---|---|
| `d["clave"]` | lanza `KeyError` |
| `d.get("clave")` | devuelve `None` |
| `d.get("clave", 0)` | devuelve `0` |

Con `[]` fallas y te enteras; con `.get()` se rellena en silencio. Elige según lo que necesites.

### Strings: son inmutables
Los métodos de string **devuelven un string nuevo**; el original no cambia. Hay que guardar el resultado.
```python
texto = "  hola\n"
texto.strip()              # se pierde el resultado
texto = texto.strip()      # 'hola'
```
- `strip()` sin argumento quita espacios, tabs y saltos de línea (`\n`).
- `strip(" ")` quita **solo espacios**.
- `repr(texto)` muestra los caracteres escondidos (`'hola\n'`). Úsalo solo para depurar, no para limpiar.

### `==` vs `is`
- `==` compara **valores**: `texto == ""`.
- `is` compara **identidad**; se usa casi solo con `None`: `if x is None`.
- `if x is "":` o `if __name__ is "__main__":` dan `SyntaxWarning`.

### `pathlib` y `shutil`
```python
from pathlib import Path
import shutil

Path("datos.db").exists()                  # ¿existe el archivo o carpeta?
Path("respaldo").mkdir(exist_ok=True)      # crea la carpeta; sin error si ya existe
Path(__file__).parent / "schema.sql"       # ruta junto al archivo actual

shutil.copy2("a.json", "respaldo")         # copia conservando fecha y metadatos
```
- `mkdir` es un método de un objeto `Path`: `Path("x").mkdir()`, no `Path.mkdir("x")`.
- Sin `exist_ok=True`, `mkdir` da `FileExistsError` si la carpeta ya existe.

### JSON y JSON Lines (`.jsonl`)
| Función | Qué hace |
|---|---|
| `json.load(archivo)` | **archivo** abierto → objeto de Python |
| `json.loads(texto)` | **string** → objeto de Python |
| `json.dump(objeto, archivo)` | objeto → escribe en un **archivo** |
| `json.dumps(objeto)` | objeto → **string** |

Un `.jsonl` tiene **un JSON por línea**, así que no sirve `json.load` sobre todo el archivo. Se recorre línea por línea:
```python
with open("datos.jsonl", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()          # quita el \n del final
        if linea == "":
            continue                   # salta líneas vacías
        try:
            registro = json.loads(linea)
        except json.JSONDecodeError:
            ...                        # línea dañada: contarla y seguir
```

[⬆ Volver al índice](#índice)


## 2. SQLite: lo que se suma

- `SELECT COUNT(*) FROM tabla WHERE col = ?` devuelve **una fila con un número**. Con `row_factory = sqlite3.Row` se lee así: `conexion.execute(sql, (valor,)).fetchone()[0]`.
- `fetchone()` devuelve una fila (o `None`); `fetchall()`, una lista de filas.
- `cursor.lastrowid`: id generado en el último `INSERT`.
- `executemany(sql, lista_de_tuplas)`: una sentencia para muchas filas.
- Los parámetros de `?` van en una **tupla**; con un solo valor lleva coma: `(x,)`.
- Nunca armes SQL con f-strings (inyección SQL): usa `?`.

[⬆ Volver al índice](#índice)


## 3. Patrón de migración de datos
1. **No pisar nada:** si el destino ya existe, detenerse.
2. **Respaldo** de los archivos de origen antes de tocar algo.
3. **Crear** el destino (tablas).
4. **Copiar** los datos conservando lo importante (por ejemplo, las fechas originales), contando los registros buenos y los inválidos.
5. **Verificar:** comparar lo que se migró con lo que realmente quedó en el destino (`COUNT(*)`).
6. Los originales **no se modifican**: si algo falla, se borra el destino y se repite.

[⬆ Volver al índice](#índice)


## 4. Git y GitHub: ramas, pull request y etiquetas

| Comando | Qué hace |
|---|---|
| `git switch -c nombre` | crea una rama y se cambia a ella |
| `git switch nombre` | cambia de rama |
| `git branch` | lista las ramas locales |
| `git push --set-upstream origin nombre` | primer push de una rama nueva (la enlaza con GitHub) |
| `git pull` | trae de GitHub lo nuevo y lo une a tu rama actual |
| `git branch -d nombre` | borra una rama ya fusionada (`-D` fuerza) |
| `git fetch --prune` | limpia referencias a ramas borradas en GitHub |
| `git log --oneline -3` | los 3 commits más recientes en una línea cada uno |
| `git tag` | lista las etiquetas |
| `git tag -a v0.2 -m "mensaje"` | crea una etiqueta anotada sobre el commit actual |
| `git push origin v0.2` | sube una etiqueta (un `push` normal **no** las sube) |
| `git show v0.1:main.py` | muestra un archivo tal como era en esa etiqueta |
| `git switch --detach v0.1` | mira todo el proyecto como era en esa versión (no hagas commits ahí; vuelve con `git switch main`) |
| `git log -1 --date=short --format=%ad v0.1` | fecha del commit al que apunta la etiqueta |

**Flujo de trabajo tipo empresa:**
1. `main` siempre estable.
2. Una rama corta por cada tarea.
3. **Pull request**: GitHub muestra todos los cambios (pestaña *Files changed*) para revisarlos antes de fusionar.
4. *Merge pull request* → *Confirm merge*.
5. `git switch main` → `git pull` → `git tag -a ...` → `git push origin ...`.
6. Borrar la rama (GitHub y local).

**Rama vs etiqueta:** una rama es una línea de trabajo que avanza; una etiqueta es un marcador **fijo** sobre un commit (una versión).

**`.gitignore`:** lo que no debe subirse (bases de datos `*.db`, entornos virtuales, cachés, datos personales). Revisa siempre `git status` y la pestaña *Files changed* antes de fusionar.

[⬆ Volver al índice](#índice)


## 5. Documentar un proyecto

**`CHANGELOG.md`:** versiones nuevas **arriba**; cada una con secciones `### Añadido`, `### Cambiado`, `### Limitaciones conocidas`.
```markdown
## [0.2] - 2026-11-11
### Añadido
- Lo nuevo que ahora existe.
```

**`README.md`:** descripción, versión actual, requisitos, instalación, uso, estructura de archivos (tabla), estado y próximos pasos.

**Markdown básico:** `#` títulos, `-` listas, `` `código` `` en línea, bloques con tres comillas invertidas, tablas con `|`. Vista previa en VS Code: `Ctrl + Shift + V`.

[⬆ Volver al índice](#índice)


## 6. Calidad de código
```bash
ruff check              # errores de estilo y de código
ruff check --fix        # arregla lo que puede (por ejemplo, el orden de imports)
ruff format --check     # ¿el formato está bien? (no modifica)
ruff format             # aplica el formato
mypy .                  # revisa los type hints en todo el proyecto
```
- Imports en orden alfabético (`I001`), dos líneas en blanco entre funciones de nivel superior, sin espacios sobrantes al final de línea.

[⬆ Volver al índice](#índice)


## 7. Errores comunes de este módulo

| Error | Causa y solución |
|---|---|
| `conexion.commit` sin hacer nada | falta `()`: sin paréntesis solo nombras la función, no la ejecutas |
| `(x)` en vez de `(x,)` | una tupla de un elemento necesita coma |
| `INSERT OR REPLACE` borra datos relacionados | borra y reinserta, y dispara `ON DELETE CASCADE`; usa `INSERT ... ON CONFLICT DO UPDATE` |
| `texto.strip()` no limpia nada | el resultado no se guardó en una variable |
| Mutar una constante compartida | una función que devuelve una constante global la comparte entre llamadas; usa `copy.deepcopy` |
| `fetchall()` vacío la segunda vez | un cursor se consume al recorrerlo; guarda la lista |
| `FOREIGN KEY constraint failed` | falta el registro padre, o falta `PRAGMA foreign_keys = ON` en esa conexión |
| `json.load` falla con `.jsonl` | no es un solo JSON: recorrer línea por línea con `json.loads` |

[⬆ Volver al índice](#índice)


---






