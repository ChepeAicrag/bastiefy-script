### Bestifey - Script
Este es un pequeño programa que tiene la finalidad de obtener las respuestas de un quiz de Bestiefy.

## Requisitos:
* Python 3.8 y superiores 

## Manual de usuario
---

### Preparar entorno de ejecución
___
1. Clonar este repositorio.

2. Se debe generar un entorno virtual de python.
```python
python -m venv env

```
3. Activar el entorno virtual generado.

```python
source env/Scripts/activate
```

4. Instalar las librerías requeridas, esto debe ser en el entorno virtual creado.
   Nota: (env) user$ es la terminal correspondiente.
   
```bash
(env) user$ pip install -r requirements.txt
```
### Obtener Quizz ID
___
1. Del enlace que te proporcionaron se obtiene el ID, este se encuentra al final del mismo cómo un argumento. Por ejemplo, del enlace https://bestiefy.com/q?=M7jb2
2. El ID del quiz es M7jb2.
3. Entonces para este ejmplo: *(QUIZ_ID=M7jb2)*
   
### Obtener API KEY
___
1. Abrir el quiz que te deseas responder. Por ejemplo: https://bestiefy.com/q?=M7jb2
2. Vamos a extrar la API KEY, para poder ejecutar el código. 
3. Clic derecho, y luego en inspeccionar. Se abrirá una ventana cómo la siguiente: 
    ![Inspeccionar elemento](images/1.jpg)
4. Dirigete a la pestaña de **Aplicación**   
5. Posteriormente, de lado derecho aparecen diferentes móulos. Accede a Storage > IndexedDB > firebaseLocalStorageDb - https://bestiefy.com y da clic en firebaseLocalStorage. Así cómo se muestra en la siguiente imagen:
    ![firebaseLocalStorage](images/2.jpg)
7. Se te desplegará información del lado derecho, vas a dar clic en **Value** y se extenderá la vista. 
    ![Values](images/3.jpg)
8. Ahora ahí aparecerá **apiKey**, copias ese valor porque es muy importante. En mi caso este valor es el que aparece en pantalla, por lo que.
   *API_KEY=AIzaSyD_rrjNxH9LfmKB0Y0uy7nSfz0zHvvM_Iw*
    ![API_KEY](images/4.jpg)

### Funcionamiento para obtener respuestas del quiz

1. Obtenido el ID del quiz y el API KEY, procedemos a ejecutar el programa en la terminal con el siguiente comando.
```python
 python bestiefy.py --quiz QUIZ_ID --key API_KEY
 ```
### Ejemplo de ejeccución
___
1. Con el ID del quiz*QUIZ_ID=M7jb2*y la key*API_KEY=AIzaSyD_rrjNxH9LfmKB0Y0uy7nSfz0zHvvM_Iw*podemos proceder a ejecutar nuestro script.
2. Por lo que el comando de ejecución es la siguiente.
```python
 python bestiefy.py --quiz M7jb2 --key AIzaSyD_rrjNxH9LfmKB0Y0uy7nSfz0zHvvM_Iw
```

3. La salida es la impresión en pantalla de un JSON con las preguntas, las respuestas, la respuestas correcta y el score de los participantes.

    ![Ejemplo de salida](images/5.jpg)

## Errores
___

1. El error que puedes tener es que el quiz no exista.
   
    ![Quiz no encontrado](images/6.jpg)
2. Qué el API_KEY esté mal, esto mostraría los errores que desencanedaría.
   
    ![Quiz no encontrado](images/7.jpg)
