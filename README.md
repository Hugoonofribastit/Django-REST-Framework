# Django-REST-Framework
*Creamos un entorno virtual y lo activamos con los siguientes comandos

python -m virtualenv venv

.\venv\Scripts\activate 

*Instalamos django
pip install django

* Instalamos el rest framework
pip install djangorestframework


* Comenzamos el proyecto con el comando

django-admin startproject drfsimplecrud .

*Ya podemos correr el servidor con

python manage.py runserver 3000

*Creamos nuestra app
python manage.py startapp projects

*Vamos a la carpeta creada "drfsimplecrud"
al archivo settings y la seccion(lista) installed apps, donde agregaremos
'projects' y el modulo 'rest_framework'

*Luego de crear nuestro modelo en project/models.py
migramos la tabla/clase a la base de datos predeterminada sqlite con los siguientes comandos

python manage.py makemigrations          (aqui la consola nos indicara que las migraciones estan en projects/migrations/001_initial.py)

python manage.py migrate (aqui ya creamos las tablas con el modelo)

ver deploy en https://drfsimplecrud-test-8e8s.onrender.com/

*Creamos serializers y api.py para setear bien los modelos de consultas y los permisos



*Creamos urls.py dentro de projects para el manejo de las urls con el router

*Luego importamos las rutas al urls.py de la carpeta drfsimplecrud


gregando el import de include y seteando el nuevo path('',include('projects.urls'))

* deploy con https://render.com/docs/deploy-django

pip freeze > requirements.txt
