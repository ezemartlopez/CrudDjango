# CrudDjango
Proyecto crud Basico con Django, Html, Css y Javascript. Para ejecutar el crud debes tener instalado pipenv, en caso de no tenerlo ejecuta el siguiente comando en tu terminal:

```bash
pip install pipenv
```
Una vez ya instalado, nos dirigimos a la carpeta que contiene `Pipfile` y `Pipfile.lock`, una vez alli ejecutamos el suiguiente comando en tu terminal:
```bash
pipenv install
```
luego activaremos el entorno virtual:
```bash
pipenv shell
```
Ahora hay que moverse hacia la carpeta `crud` que contiene el archivo `manage.py`, con el siguiente comando en tu terminal:
```bash
cd crud
```
Ahora corremos la aplicacion Django con el siguiente comando (en windows) en tu terminal:
```bash
python manage.py runserver
```
Puedes abrir la aplicacion en tu navegador en `localhost:8000`. Para cerrar el servidor simplemente ajecuta `Ctr-C` mientras estas en la terminal y para cerrar el entorno virtual simplemente ejecuta el siguiente comando:
```bash
exit
```
