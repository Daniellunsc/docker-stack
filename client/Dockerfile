FROM node:latest

RUN mkdir app
WORKDIR /app

COPY ./ /app/

RUN cat package.json
RUN npm install
CMD ["npm", "start"]

