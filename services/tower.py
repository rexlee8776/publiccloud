from contextlib import closing
import socket
import random
import uuid
import json

from kubernetes import client, config
import yaml


y_deployment = {
  "apiVersion": "extensions/v1beta1",
  "kind": "Deployment",
  "metadata": {
    "name": "yardstick-service-default"
  },
  "spec": {
    "replicas": 1,
    "template": {
      "metadata": {
        "labels": {
          "app": "yardstick-service-default"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "yardstick-k8s",
            "image": "rexlee8776/yardstick:service",
            "ports": [
              {
                "containerPort": 5000
              }
            ],
            "volumeMounts": [
              {
                "mountPath": "/var/run/docker.sock",
                "name": "docker-sock"
              }
            ]
          }
        ],
        "volumes": [
          {
            "name": "docker-sock",
            "hostPath": {
              "path": "/var/run/docker.sock"
            }
          }
        ]
      }
    }
  }
}
y_service = {
  "apiVersion": "v1",
  "kind": "Service",
  "metadata": {
    "name": "yardstick-service-default"
  },
  "spec": {
    "ports": [
      {
        "port": 5000
      }
    ],
    "selector": {
      "app": "yardstick-service-default"
    },
    "type": "NodePort"
  }
}


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
        service_name = "yardstick-service-" + str(uuid.uuid4()).split('-')[0]
        y_deployment['metadata']['name'] = service_name
        y_deployment['spec']['template']['metadata']['labels']['app'] = service_name
        y_service['metadata']['name'] = service_name
        y_service['spec']['selector']['app'] = service_name
        print "***y_deployment = \n%s\n" % json.dumps(y_deployment, indent=4)
        print "***y_service = \n%s\n" % json.dumps(y_service, indent=4)
        config.load_kube_config(config_file='/etc/kubernetes/admin.conf')
        # create deployment
        extensions_v1beta1 = client.ExtensionsV1beta1Api()
        ## with open('/tmp/yardstick.yaml', 'r') as f:
        ##     deployment = yaml.load(f)
        create_deployment(extensions_v1beta1, y_deployment)
        # create service
        ## with open('/tmp/service.yaml', 'r') as f:
        ##     service = yaml.load(f)
        core_v1_api = client.CoreV1Api()
        create_service(core_v1_api, y_service)
        result = core_v1_api.read_namespaced_service(service_name, 
                  namespace="default")
        y_service_port = str(result.spec.ports[0].node_port)
        print "service name is %s" % service_name
        print "service port is %s" % y_service_port
        print ("*****************Server works OK!!!*******************\n")
        return "http://172.16.10.150:%s/gui/index.html" % y_service_port


    def delete(self):
        print "delete a deployment begin"
        print "delete a deployment end"


if __name__ == "__main__":
    print "test yardstick service"
