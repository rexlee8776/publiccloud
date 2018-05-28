# This file works to install yardstick service


# set Yardstick Service Variables
PROJECT_NAME=yservice
YSERVICE_HOME=/home/publiccloud
CONF_DIR=etc/${PROJECT_NAME}
LOG_DIR=/var/log/${PROJECT_NAME}
cd ${YSERVICE_HOME}

#apt-get update

# install supervisor
# apt-get install -y supervisor
cp ${CONF_DIR}/supervisor.conf /etc/supervisor/conf.d/

# install nginx
# apt-get install -y nginx
touch /var/run/yservice.sock
chmod 666 /var/run/yservice.sock

# config ngix and reload
rm /etc/nginx/conf.d/*.conf
cp ${CONF_DIR}/yservice.conf /etc/nginx/conf.d/
service nginx reload

# install uwsgi
# apt-get install -y uwsgi
mkdir -p /${CONF_DIR}
cp yservice-db.sqlite3 /${CONF_DIR}/
mkdir -p ${LOG_DIR}

# install python dependency
# apt-get install -y python-pip
pip install -r requirements.txt

# restart uwsgi
cp ${CONF_DIR}/yservice.ini /${CONF_DIR}/yservice.ini
uwsgi -i /${CONF_DIR}/yservice.ini
