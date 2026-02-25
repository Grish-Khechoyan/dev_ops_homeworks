#!/bin/bash

sudo apt update 
sudo apt install nginx -y

cd /var/www/html/

for i in {1..3}; do 
   sudo touch "page$i.html";
   sudo chmod 644 "page$i.html";
   sudo chown www-data:www-data "page$i.html";
done


if systemctl is-active --quiet nginx; then
   	echo "NGINX is running."
    # Runing if the service is active
	sudo systemctl restart nginx

else
    	echo "NGINX not running."
    # Runing if the service is not active
    	sudo systemctl start nginx
fi

sudo journalctl -u nginx -n 5
