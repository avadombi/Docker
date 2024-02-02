# 1. Subject

Develop a Python application that reads an xlsx file and plot a figure.
## 1.1. Needs:

### 1.1.1. Use Python image

In your Dockerfile
FROM python:tag

### 1.1.2. Dependencies
* pandas
* matplotlib
* openpyxl
* xlrd

Store in a requirement.txt document
In your Dockerfile:

// Copy requirements.txt file
COPY requirements.txt /app/requirements.txt

// Install dependencies
RUN pip install -r /app/requirements.txt

### 1.1.3. Data consistency
Use the concept of docker volume to bind your local folder that contains the csv to a container folder that will reference to that file.

How to?
When building your image
docker run -it -v path_to_local_data_folder:path_to_container_data_folder name_image:tag
it: interactive (STDIN) => let the user provide entries for e.g.

In your python file:
data = pd.read_xlsx('path_to_container_data_folder/data.xlsx')


# 2. The steps

## 2.1. Local organization of our project
## 2.1.1. Create a project folder

Project folder's name: PythonPandas

## 2.1.2. Create a folder that contains our data
Name: data
In this, place the xlsx file

## 2.1.3. Create a folder that contains our script
Name: scripts
In this, create a python file named main.py

## 2.1.4. Create a folder that contains our requirements
Name: requirements
In this, create a file named: requirements.txt and add requirements

## 2.2. Docker side
### 2.2.1. Create a Dockerfile

This Dockerfile will pull a python environment that we will use to install our dependencies and allow our script to run conformly.
A the project root (here, just below PythonPandas), create a Dockerfile

NOTE: As there should only have one FROM instruction in a Dockerfile, if your app use many differents base image, then you should divide your app into the corresponding base image, then use one of the following approch to make the corresponding container communicating.

Voici quelques-unes des méthodes couramment utilisées pour permettre la communication entre conteneurs :

Réseaux Docker : Vous pouvez créer un réseau Docker dédié et connecter les conteneurs à ce réseau. Les conteneurs connectés au même réseau peuvent communiquer entre eux en utilisant leurs noms de conteneur comme noms d'hôte ou en utilisant des adresses IP. Vous pouvez créer un réseau Docker en utilisant la commande docker network create et connecter les conteneurs à ce réseau en utilisant l'option --network lors du démarrage du conteneur.

Résolution de noms DNS : Docker fournit un service de résolution de noms DNS intégré pour les conteneurs. Chaque conteneur Docker est automatiquement enregistré dans le serveur DNS interne de Docker et peut être résolu par son nom de conteneur. Ainsi, vous pouvez faire référence à d'autres conteneurs en utilisant leur nom de conteneur comme nom d'hôte dans vos applications.

Exposition de ports : Si vous avez des services ou des applications qui écoutent sur des ports spécifiques à l'intérieur des conteneurs, vous pouvez exposer ces ports sur l'hôte Docker à l'aide de l'option -p lors du démarrage du conteneur. Ainsi, d'autres conteneurs ou applications externes peuvent accéder aux services exposés en se connectant à l'adresse IP et au port de l'hôte Docker.

Services d'orchestration de conteneurs : Si vous travaillez avec un orchestrateur de conteneurs comme Docker Swarm, Kubernetes ou Amazon ECS, ces outils fournissent des fonctionnalités avancées pour la gestion et la communication des conteneurs. Ils permettent de définir des services, des règles de communication, des équilibrages de charge, etc., facilitant ainsi la communication entre conteneurs.


**NOTE**
Sometimes, a image can fail when building it and the space used is not freed. To free it, use the following command

(below seem not to do what we want)
docker builder prune --all -f  // remove build cache
OR
docker image prune

To see more options:
docker builder





