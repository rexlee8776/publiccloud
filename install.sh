rm /etc/nginx/conf.d/*.conf
#apt-get update

# install supervisor
# apt-get install -y supervisor
cp docker/supervisor.conf /etc/supervisor/conf.d/

# install nginx
# apt-get install -y nginx
touch /var/run/yardstick-service.sock
chmod 666 /var/run/yardstick-service.sock
cp docker/yardstick-service.conf /etc/nginx/conf.d/
service nginx reload

# install uwsgi
# apt-get install -y uwsgi
mkdir -p /var/log/yardstick-service/

# install python dependency
# apt-get install -y python-pip
pip install -r requirements.txt

# restart uwsgi
uwsgi -i /home/publiccloud/docker/yardstick-service.ini
