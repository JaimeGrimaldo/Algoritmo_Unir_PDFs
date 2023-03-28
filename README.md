# Módulo para unir PDFs
En este repositorio encontraremos el algoritmo elaborado en **Python** con el cual podremos unir PDFs

## Tecnologías usadas
La tecnología usada es la siguiente:
1. Python: 3.7.9
2. pip 20.1.1

___

## Instrucciones de uso
1. Para poder correr el programa exitosamente, primeramente deberemos de crear un entorno virtual con el siguiente comando:
~~~
python -m venv (nombre del entorno)
~~~
2. Desde luego deberemos de estar ubicados dentro de nuestra carpeta del proyecto/raíz de proyecto.

**No olvides arrancar el entorno virtual con**
~~~
carpetaProyecto\nombreEntorno\Scripts\activate
~~~
Con esto ya tendremos el entorno activado y podremos ir al siguiente paso.

3. Una vez creado el entorno virtual necesitaremos instalar PyPDF2 en su versión 2.12.2. **IMPORTANTE QUE SEA ESTA VERSIÓN** Las versiones más recientes de eta librería
dan enormes problemas, cambiando totalmente la manera de hacerlo. En diversos foros de discusión para solucionar bugs, mismos programadores recomiendan usar una versión anterior.

~~~
pip install PyPDF2==2.12.2
~~~
Importante instalar tal como está escrito en el comando dado, ya que si variamos entre mayúsculas o minúsculas nos instala otra librería diferente que no nos sirve.

___

### Listo para correr programa
Con esto ya tendremos suficiente para el arranque del programa, solamente ingresamos el nombre de nuestro archivo *main.py* en el CMD (teniendo activado el entorno virtual) y el programa no dará ningún mensaje vía consola. Solamente se generará un nuevo archivo dentro de la raíz del proyecto con la unificación de los PDFs

### Ruteo de PDFs
Los PDFs ingresados deben estar en una ruta que conozcamos. Al menos yo los dejo ahí. En al línea de código 3 encontraremos ese array de PDfs, en donde deberemos de cambiar el nombre a nuestros PDfs que necesitamos fusionar. En la siguiente línea pondremos como se llamara el PDF final y listo, tan simple como eso. 
