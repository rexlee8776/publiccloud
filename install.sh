apt-get update

# install supervisor
apt-get install -y supervisor
cp docker/supervisor.conf /etc/supervisor/conf.d/

# install nginx
apt-get install -y nginx
touch /var/run/publiccloud.sock
chmod 666 /var/run/publiccloud.sock
cp docker/publiccloud.conf /etc/nginx/conf.d/
service nginx reload

# install uwsgi
apt-get install -y uwsgi
mkdir -p /var/log/publiccloud

# install python dependency
apt-get install -y python-pip
pip install -r requirements.txt

# restart uwsgi
uwsgi -i /home/publiccloud/docker/publiccloud.ini
