# This file works to install yardstick service


# set Yardstick Service Variables
PROJECT_NAME=yservice
YARDSTICK_SERVICE_HOME=/home/publiccloud
cd ${YARDSTICK_SERVICE_HOME}

#apt-get update

# install supervisor
# apt-get install -y supervisor
cp docker/supervisor.conf /etc/supervisor/conf.d/

# install nginx
# apt-get install -y nginx
touch /var/run/yservice.sock
chmod 666 /var/run/yservice.sock

# config ngix and reload
rm /etc/nginx/conf.d/*.conf
cp docker/yservice.conf /etc/nginx/conf.d/
service nginx reload

# install uwsgi
# apt-get install -y uwsgi
mkdir -p /etc/${PROJECT_NAME}
cp yservice-db.sqlite3 /etc/${PROJECT_NAME}/
mkdir -p /var/log/${PROJECT_NAME}

# install python dependency

# apt-get install -y python-pip
pip install -r requirements.txt
# restart uwsgi
uwsgi -i docker/yservice.ini
