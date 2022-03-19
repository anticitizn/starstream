FROM node:16-alpine
WORKDIR ./frontend
COPY package*.json ./
RUN npm install
COPY . .
#RUN npm install --verbose vite
#RUN npm install --verbose -g @vue/cli
CMD ["npm", "run", "dev", "--host"]