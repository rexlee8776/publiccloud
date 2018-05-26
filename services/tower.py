from contextlib import closing
import socket
import random

from docker import Client
from kubernetes import client, config
import yaml


def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def get_free_port(ip):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        port = random.randint(9000, 9200)
        while s.connect_ex((ip, port)) == 0:
            port = random.randint(9000, 9200)
        return port


def _create_influxdb_container(client, name, port):

    consts = {"INFLUXDB_IMAGE": 'tutum/influxdb',
              "INFLUXDB_TAG": '0.13'}
    ports = [port]
    port_bindings = {8086: port}
    restart_policy = {"MaximumRetryCount": 0, "Name": "always"}
    host_config = client.create_host_config(port_bindings=port_bindings,
                                            restart_policy=restart_policy)

    print("Creating container with binding port %s" % port)
    container = client.create_container(image='%s:%s' %
                                        (consts["INFLUXDB_IMAGE"],
                                         consts["INFLUXDB_TAG"]),
                                        ports=ports,
                                        name=name,
                                        detach=True,
                                        tty=True,
                                        host_config=host_config)
    print('Starting container')
    client.start(container)
    return container


def _create_yardstick_container(client, name, port):

    consts = {"IMAGE": 'opnfv/yardstick',
              "TAG": 'stable'}
    ports = [port]
    port_bindings = {5000: port}
    restart_policy = {"MaximumRetryCount": 0, "Name": "always"}
    volume = '/var/run/docker.sock'
    volumes = [volume]
    host_config = client.create_host_config(port_bindings=port_bindings,
                                            restart_policy=restart_policy,
                                            binds=["%s:%s" % (volume, volume)])

    print("Creating container with binding port %s" % port)
    container = client.create_container(image='%s:%s' %
                                        (consts["IMAGE"],
                                         consts["TAG"]),
                                        ports=ports,
                                        volumes=volumes,
                                        name=name,
                                        detach=True,
                                        tty=True,
                                        host_config=host_config)
    print('Starting container')
    client.start(container)


class K8SService(object):
    @classmethod
    def create_service(cls, name, user):
        pod = Pod(name, user)
        return pod.create()


class Pod(object):
    def __init__(self, name, user):
        self.name = name
        self.user = user

    def create(self):
        # print ("service name is '%s' and user is '%s'" % (self.name, self.user))
        # print get_free_port('172.17.0.1')
        # yardstick_name = "yardstick_" + self.name
        # influxdb_name = "influxdb_" + self.name
        # grafana_name = "grafana_" + self.name
        # yardstick_port =  get_free_port('172.17.0.1')
        # client = Client('unix://var/run/docker.sock')
        # _create_yardstick_container(client, yardstick_name ,yardstick_port)

        config.load_kube_config(config_file='/etc/kubernetes/admin.conf')
        extensions_v1beta1 = client.ExtensionsV1beta1Api()

        with open('/tmp/yardstick.yaml', 'r') as f:
            deployment = yaml.load(f)
        create_deployment(extensions_v1beta1, deployment)
        yardstick_port = 5000
        return "http://172.16.10.137:%s/gui/index.html" % yardstick_port


if __name__ == "__main__":
    print get_free_port('172.17.0.1')
