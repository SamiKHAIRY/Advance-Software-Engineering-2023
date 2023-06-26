FROM node:12-alpine
RUN apk add --no-cache python2 g++ make git
RUN git clone https://github.com/docker/getting-started.git
WORKDIR /getting-started/app
RUN npm install 
EXPOSE 3000
CMD ["node", "src/index.js"]