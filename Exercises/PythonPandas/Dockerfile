# base image: python (to get the right tag, go to docker hub and search)
FROM python:3.9

# copy requirements file in /app/
COPY requirements /app/

# copy the content all contents in /app
COPY scripts /app/

# copy data
COPY data /app

# specify your working directory
WORKDIR /app

# install dependencies
# RUN pip install -r requirements.txt
# RUN pip install pandas && pip install matplotlib && pip install openpyxl && pip install xlrd
RUN pip install --no-cache-dir -r requirements.txt

# execute the script
CMD ["python", "main.py"]


