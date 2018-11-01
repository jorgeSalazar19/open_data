# Datos Abiertos Producción de cacao
este es un respositorio para un proyecto de la asignatura cliente servidor, en el cual se busca consumir recursos de datos abiertos luego de hacer login con la api de github.

## Pasos para instalación del proyecto
1. Primero descargar el repositorio en su PC por medio del comando ``` git clone repo_link ```, recuerde que el repo link se obtiene en la sección de descarga del repo en github.

1. Una vez descargado el repo, se debe crear un entorno virtual con python 3, a continuación un ejemplo de como crear un entorno virtual con virtualens:

  1. con el siguiente comando se crea el entorno virtual - ```virtualenv -p /usr/bin/python3 nombre_entorno```  .
  
  1. luego se procede a activarlo son el siguiente comando ```source bin/activate```, recuerde este comando solo          funciona si se esta dentro de la carpeta del entorno vistural creado. 
  
1. Una vez creado y activado el entorno virtual nos dirigimos a la carpeta que acabamos de descargar del repo en nuestro caso se llama open_data, una vez ahi ejecutamos el comando ```pip install -r requirements.txt``` el cual instalara las dependencias para que el proyecto funcione.

1.luego de esto se debe crear una base de datos de postgres con el nombre de open_data, visualizar el siguiente link para ver como crear base de datos https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

1. Una vez creada la base de datos procedemos a correr las migraciones pertinentes con el siguiente comando ```python manage.py migrate```.

1. Finalmente corremos el proyecto con el siguiente comando ```python manage.py runserver```.

siguiendo estos pasos podremos correr nuestro proyecto de datos abiertos.

link del tutorial que comtiene la información con la que fue desarrollado este proyecto https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html

