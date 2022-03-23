FROM node:16-bullseye
RUN apt-get update
RUN apt-get install iputils-ping -y
WORKDIR ./frontend
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "run", "dev", "--host"]