FROM node:16.14.0

WORKDIR /user/src/app

COPY ./package.json ./

COPY ./yarn.lock ./

RUN npm install 

COPY . .

EXPOSE 3000

CMD ["npm" , "start"]