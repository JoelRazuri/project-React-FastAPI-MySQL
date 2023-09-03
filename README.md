# project-React-FastAPI-MySQL

--- BACKEND ---

ENTORNO VIRTUAL
Instalar entorno virtual para Python: 
Ej: virtualenv
'pip install virtualenv'

Crear entorno virtual dentro de la carpeta 'backend':
'virtualenv env'

Iniciar el entorno virtual:
'source env/Scripts/activate'

DEPENDENCIAS
Instalar dependencias:
'pip install -r requirements.txt'

SERVER
Inicar servidor Uvicorn desde la carpeta 'backend':
'uvicorn app.app:app --reload'

VARIABLES DE ENTORNO
Crear archivo '.env' dentro de la carpeta 'backend/app'

Contenido del archivo '.env':
URL_CONNECTION = mysql://root:{password}@localhost:{port}/{nameBDD}
Ej: 
URL_CONNECTION = mysql://root:4321@localhost:3306/project3

BASE DE DATOS MYSQL
La base de datos 'nameBDD' ya tiene que estar creada
