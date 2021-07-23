FROM node:16-alpine3.11
WORKDIR /react
COPY . .
COPY package.json ./package.json
COPY package-lock.json ./package-lock.json
RUN npm install
RUN npm run build