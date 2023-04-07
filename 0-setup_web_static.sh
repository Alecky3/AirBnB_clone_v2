#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "This is a test deployment" | sudo tee /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
mkdir -p /var/www/test/html
touch /var/www/test/html/index.html
echo "Hello World!" > /var/www/test/html/index.html
touch /var/www/test/html/404.html
echo "Ceci n'est pas une page" > /var/www/test/html/404.html
printf %s "server {
     listen      80 default_server;
     listen      [::]:80 default_server;
     root        /var/www/test/html;
     index       index.html index.htm;

     location /redirect_me {
        return 301 'https://www.youtube.com/watch?v=QH2-TGUlwu4';
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/test/html;
      internal;
	}
    location /hbnb_static/ {
    	alias /data/web_static/current/;
    }
}
" > /etc/nginx/sites-available/default/
sudo service nginx start
