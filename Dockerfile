FROM node:lts-alpine3.12 as build

WORKDIR /temp

COPY . . 

RUN npm install && \
        npm run build

FROM nginx:latest

WORKDIR /usr/src/app

COPY --from=build /temp/dist/ . 

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]