>El readme está en ingles y en español.

# Information system to register voter data from the municipalities of Colombia.

A REST API written with [Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/).


#  Description of the solution
The approach of splitting the project's responsibilities into different apps was taken to make the project easier to scale and as modular as possible. For the database, an image of a SQL database deployed in a Docker container was used.

The project consists of a total of 4 apps: login, locations, users, and voters.

Login
--
This app is responsible for validating credentials and generating the token. It has login and logout views. The token is associated with the validated user.

Locations
--
It handles the creation of the voting booth models, as well as those of municipality and department. It also takes care of calling the external API for georeferencing.

Users
--
This part is responsible for creating the user models. Since the admin and leader models had fields not shared between them, another auxiliary table called 'user' was created to store the data used for authentication

Voters
--
It handles the management of the voters' model, as well as the generation of the necessary views as per the requirements.


# Initial Configuration
**Prerequisite: [Docker](https://docs.docker.com/engine/install/) must be installed.**

1.- Clone this repository:
 
	https://github.com/Nemesis1019/ManageVotingSystem.git

  
2.- Create a virtual environment (It is recommended to avoid version conflicts in packages) :

	python virtualenv .venv

3.- Active virtual environment.

**-Linux:**

	source .venv/bin/activate
**-Windows:**

	source .venv/Scripts/activate
  

4.- Install libraries.

  

	pip install -r requirements.txt

5 Start the Docker container. 
				
	docker-compose u


6.- Run commands:

	python manage.py makemigrations|
	python manage.py migrate
	python manage.py runserver

The local server should be running.

# Sistema de información para registrar datos de votantes de los municipios de Colombia.

Una API REST escrita con [Django](https://www.djangoproject.com/) y [Django Rest Framework](https://www.django-rest-framework.org/).

## Descripción de la solución

Se tomó el enfoque de dividir las responsabilidades del proyecto en distintas aplicaciones para que el proyecto sea más fácil de escalar y lo más modular posible. Para la base de datos, se utilizó una imagen de una base de datos SQL desplegada en un contenedor Docker.

El proyecto consta de un total de 4 aplicaciones: login, locations, users y voters.

### Login

Esta aplicación se encarga de validar las credenciales y generar el token. Tiene vistas de inicio de sesión y cierre de sesión. El token se asocia con el usuario validado.

### Locations

Se encarga de la creación de los modelos de mesa de votación, así como los de municipio y departamento. También se encarga de llamar a la API externa para la georreferenciación.

### Users

Esta parte se encarga de crear los modelos de usuarios. Dado que los modelos de admin y líder tenían campos no compartidos entre ellos, se creó otra tabla auxiliar llamada 'user' para almacenar los datos utilizados para la autenticación.

### Voters

Se encarga del manejo del modelo de los votantes, así como de la generación de las vistas necesarias según los requisitos.

## Configuración inicial

**Prerrequisito: [Docker](https://docs.docker.com/engine/install/) debe estar instalado.**

1.  Clonar este repositorio:
    

    `https://github.com/Nemesis1019/ManageVotingSystem.gitt` 
    
2.  Crear un entorno virtual (se recomienda para evitar conflictos de versión en los paquetes):
    
    
    `python virtualenv .venv` 
    
3.  Activar el entorno virtual.
    
    **Linux:**
    
    
    `source .venv/bin/activate` 
    
    **Windows:**
    
    
    `source .venv/Scripts/activate` 
    
4.  Instalar las bibliotecas.
    
    
    `pip install -r requirements.txt` 
    
5.  Iniciar el contenedor Docker.
    
   
    
    `docker-compose up` 
    
6.  Ejecutar los comandos:
    
 
    
	    python manage.py makemigrations
	    python manage.py migrate
	    python manage.py runserver` 
    

El servidor local debería estar funcionando.
