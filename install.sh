SERVICE_NAME=yardstick-service
YARDSTICK_SERVICE_HOME=/home/opnfv/repos/${SERVICE_NAME}

rm /etc/nginx/conf.d/yardstick.conf
#apt-get update

# install supervisor
# apt-get install -y supervisor
cp docker/supervisor.conf /etc/supervisor/conf.d/

# install nginx
# apt-get install -y nginx
sock_file=/var/run/${SERVICE_NAME}.sock
touch ${sock_file}
chmod 666 ${sock_file}
cp docker/${SERVICE_NAME}.conf /etc/nginx/conf.d/
service nginx reload

# install uwsgi
# apt-get install -y uwsgi
mkdir -p /var/log/${SERVICE_NAME}

# install python dependency
# apt-get install -y python-pip
pip install -r requirements.txt

# restart uwsgi
uwsgi -i ${YARDSTICK_SERVICE_HOME}/docker/${SERVICE_NAME}.ini
