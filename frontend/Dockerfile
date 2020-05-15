FROM node:carbon-slim
# vue-cli reqires 8.10.0+ 

RUN apt-get -y update \
  && apt-get install -y git

RUN npm install -g @vue/cli

WORKDIR /src

EXPOSE 8080

USER node

ENV CHOKIDAR_USEPOLLING=true

CMD ["yarn", "serve"]
