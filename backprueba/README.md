## Detalles del proyecto
- Python
- Django
- SQL Server

## Instrucciones de Despliegue Local desde cero
- Para realizar la verificación de los puntos de la prueba técnica se deben seguir los siguientes pasos:

- Clonar el proyecto, ya sea con el comando git clone https://github.com/shelvinbb903/PruebaWVI.git o usando una herramienta grafica GitHub y acceder a la carpeta backprueba desde una terminal de comandos.

- Activar enviroment de python con los comandos:

`vpython -m venv env
source env/Scripts/activate
Instalar las dependencias necesarias y usadas para la prueba con el comando: pip install -r requirements.txt`

- Cambiar la conexión a la base de datos archivo PruebaTecnica/settings.py del proyecto. En este archivo se modifican el diccionario u objeto DATABASES, el cual tiene los atributos para la conexión establecida por defecto. Se modifican los atributos USER y PASSWORD y NAME que corresponde al nombre de la base de datos que generó en el paso anterior.

- Para esta prueba tecnica ya se usa la conexion suministrada.

- En este punto, el proyecto está listo para realizar prueba. Se realiza la ejecución con el comando: python manage.py runserver

## Nota Adicional
La url local que usa Django es http://localhost:8000 o http://127.0.0.1:8000