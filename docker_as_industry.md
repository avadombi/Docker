# 1. Subject

Develop a Python application that reads a csv file and plot a figure.
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
data = pd.read_csv('path_to_container_data_folder/data.csv')




