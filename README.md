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

---

## Estilo de código (PEP 8)

- 4 espacios por nivel de sangría; consistente dentro de cada bloque.
- **Dos** líneas en blanco entre funciones y entre una constante y el primer `def`.
- En argumentos con nombre, sin espacios alrededor del `=`: `encoding="utf-8"`.
- Sin espacios sobrantes al final de las líneas ni líneas vacías de más al final del archivo.
- Nombres que dicen lo que guardan: `texto_sin_tildes`, no `letras_tilde`.










