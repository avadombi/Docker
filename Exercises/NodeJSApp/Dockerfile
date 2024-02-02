# Dockerfile for node.js app

# Base image to use. This will install node.js and npm
FROM node:19-alpine

# get application files, codes
# here, we copy package.json file and add it to the filesystem of the container at path <desc> = /app/
# Note: COPY is executed on the host
# the folder "app" will be created if not exists.
# do not forget the / at the end.
COPY package.json /app/

# copy the CONTENT of the directory src
COPY src /app/

# go to /app/ directory before installing express
# WORKDIR ~ cd in cmd
WORKDIR /app

# Install the dependencies of our app (see package.json)
# Note: RUN is executed in the container
RUN npm install

# define the default command to execute when the app starts
# if it was python, CMD ["python", "app.py"]
# only one CMD in a Dockerfile
CMD ["node", "server.js"]

