
# matployDraw  

con MatployDraw se aplica la librería matploy para la generación de gráficos estadísticos masivos a partir de la lectura de datos en formato json.

En la demo (demo.py) vemos que tan solo nos pide la ubicación de los datos Json ("/data/data.json") y la ruta donde queremos que se guarden los gráficos generados ("/images/").

### Configuración del entorno de desarrollo.
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 |  Crear el entorno de trabajo.     | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Prepare la receta de librerías.   | pip install -r requirements.txt     |
| Paso 5 | Demostración de uso. | py demo.py |

### Librerías del proyecto.
| librería  | Descripción              | Comando                           |
| :----     | :---                     | :---                              |
| matplotlib | Permite crear gráficos de líneas | pip install matplotlib|

Con la instalación de la librería matplotlib se instalarán las
siguientes librerías de manera automática:
<pre>
contourpy==1.1.1
cycler==0.12.1
fonttools==4.51.0
importlib_resources==6.4.0
kiwisolver==1.4.5
matplotlib==3.7.5
numpy==1.24.4
packaging==24.0
pillow==10.3.0
pyparsing==3.1.2
python-dateutil==2.9.0.post0
six==1.16.0
zipp==3.18.1
</pre>

### Realice sus pruebas, actualizaciones o modificaciones.
Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3. No esta permitido modificar la licencia de trabajos derivados de este proyecto. Por norma internacional debes conservar el mismo tipo de licencia.

#### Actualizar la receta.
Si agregas nuevas librerías al proyecto, no olvides actualizar la receta.

``` CMD
pip freeze > requirements.txt
```
#### Comprobar que todo está en orden.
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior.                  | rm -R env                             |
| Paso 3 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 4 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 5 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 6 | Instale las librerías necesarias para operar. | pip install -r requirements.txt       |
| Paso 7 | Pruebe los cambios realizados.| py demo.py |
| Paso 8 | Finalice su gestión.                          | deactivate                            |
