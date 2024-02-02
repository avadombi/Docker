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

In your python file:
data = pd.read_xlsx('path_to_container_data_folder/data.xlsx')


# 2. The steps

## 2.1. Local organization of our project
## 2.1.1. Create a project folder

Project folder's name: PythonPandas

## 2.1.2. Create a folder that contains our data
Name: Data
In this, place the xlsx file

## 2.1.3. Create a folder that contains our script
Name: Scripts
In this, create a python file named plot_xy.py

## 2.1.4. Create a folder that contains our requirements
Name: Requirements
In this, create a file named: requirements.txt and add requirements







