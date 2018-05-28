from contextlib import closing
import socket
import random

from kubernetes import client, config
import yaml


def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def create_service(api_instance, service):
    # Create deployement
    api_response = api_instance.create_namespaced_service(
        body=service,
        namespace="default")
    print("Service created. status='%s'" % str(api_response.status))


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

        print ("\n*****************Server works OK!!!*******************")
        config.load_kube_config(config_file='/etc/kubernetes/admin.conf')
        # create deployment
        extensions_v1beta1 = client.ExtensionsV1beta1Api()
        with open('/tmp/yardstick.yaml', 'r') as f:
            deployment = yaml.load(f)
        create_deployment(extensions_v1beta1, deployment)
        # create service
        with open('/tmp/service.yaml', 'r') as f:
            service = yaml.load(f)
        core_v1_api = client.CoreV1Api()
        create_service(core_v1_api, service)
        yardstick_port = 5000
        print ("*****************Server works OK!!!*******************\n")
        return "http://172.16.10.137:%s/gui/index.html" % yardstick_port


    def delete(self):
        print "delete a deployment begin"
        print "delete a deployment end"



if __name__ == "__main__":
    print "test yardstick service"
