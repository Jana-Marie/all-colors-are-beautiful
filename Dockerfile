FROM nginx:alpine
COPY ./static /usr/share/nginx/html
EXPOSE 5033
CMD ["/bin/sh", "-c", "sed -i 's/listen  .*/listen 5033;\\ncharset utf-8;/g' /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]