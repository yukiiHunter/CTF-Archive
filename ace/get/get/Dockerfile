FROM node:alpine

WORKDIR /app
COPY index.js .


RUN npm install express
EXPOSE 3000

ENTRYPOINT [ "node", "index.js" ]
