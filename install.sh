# This file works to install yardstick service


# set Yardstick Service Home
YARDSTICK_SERVICE_HOME=/home/publiccloud

#apt-get update

# install supervisor
# apt-get install -y supervisor
cp docker/supervisor.conf /etc/supervisor/conf.d/

# install nginx
# apt-get install -y nginx
touch /var/run/yardstick-service.sock
chmod 666 /var/run/yardstick-service.sock

# config ngix and reload
rm /etc/nginx/conf.d/*.conf
cp docker/yardstick-service.conf /etc/nginx/conf.d/
service nginx reload

# install uwsgi
# apt-get install -y uwsgi
mkdir -p /var/log/yardstick-service/

# install python dependency

cd ${YARDSTICK_SERVICE_HOME}
# apt-get install -y python-pip
pip install -r requirements.txt
# restart uwsgi
uwsgi -i docker/yardstick-service.ini
