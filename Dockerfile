FROM nginx:alpine
COPY index.html styles.css /usr/share/nginx/html/
COPY images /usr/share/nginx/html/images/
EXPOSE 80
