FROM node:16-slim
WORKDIR /usr/node/app
COPY ./package.json /usr/node/app 
COPY ./index.js /usr/node/app 
RUN npm install
EXPOSE 3070
CMD ["node", "index.js"]