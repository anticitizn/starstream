FROM node:16-alpine
WORKDIR ./
COPY . ./
RUN npm install
RUN npm install --verbose vite
RUN npm install --verbose -g @vue/cli
CMD ["npm", "run", "dev"]